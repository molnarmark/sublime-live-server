import sublime
import sublime_plugin
import subprocess
import os, webbrowser

SETTINGS_FILE = 'LiveServer.sublime-settings'
SERVER_BINARY_PATH = '/live-server/live-server.js'
PLUGIN_NODE_PATH = os.path.join(
  os.path.dirname(os.path.realpath(__file__)),
  SERVER_BINARY_PATH
)

SERVER_PROCESS = None
RUNNING_ON_PORT = None

RUNNING_STATUS_MESSAGE = 'Live Server ✔️'
STATUS_KEY = 'live_server_status'

class LiveServerEventListener(sublime_plugin.ViewEventListener):
  def on_activated(self):
    if SERVER_PROCESS:
      self.view.set_status(STATUS_KEY, RUNNING_STATUS_MESSAGE)
    else:
      self.view.erase_status(STATUS_KEY)

class LiveServerStartCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    global SERVER_PROCESS, RUNNING_ON_PORT
    if SERVER_PROCESS:
      SERVER_PROCESS.terminate()

    settings = sublime.load_settings(SETTINGS_FILE)
    project_path = self.view.window().project_data()['folders'][0]['path']

    args = [
      '--port={}'.format(settings.get('port')),
      '--address={}'.format(settings.get('address')),
      '--cors={}'.format(settings.get('cors')),
      '--ignore={}'.format(settings.get('ignore'))
    ]

    live_server_path = settings.get('global_node_modules_path') + PLUGIN_NODE_PATH
    SERVER_PROCESS = subprocess.Popen(
      [settings.get('node_executable_path'), live_server_path, project_path] + args,
      stdout=subprocess.PIPE,
      stdin=subprocess.PIPE,
      stderr=subprocess.PIPE,
      env=os.environ.copy(),
      startupinfo=None,
    )

    RUNNING_ON_PORT = settings.get('port')

    self.view.window().status_message('🎉 Live Server running on {}.'.format(settings.get('port')))
    self.view.set_status(STATUS_KEY, RUNNING_STATUS_MESSAGE)

class LiveServerStopCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    global SERVER_PROCESS
    SERVER_PROCESS.terminate()
    SERVER_PROCESS = None
    self.view.window().status_message('❌ Live Server stopped.')
    self.view.erase_status(STATUS_KEY)

class LiveServerOpenInBrowserCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if SERVER_PROCESS:
      self.view.window().status_message('📖 Opening Live Server..')
      webbrowser.open('http://localhost:{}'.format(RUNNING_ON_PORT))
    else:
      self.view.window().status_message('❌ Live Server isn\'t running. Nothing to open.')
