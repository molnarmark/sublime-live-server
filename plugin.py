import sublime
import sublime_plugin
import subprocess
import os, time

SETTINGS_FILE = 'LiveServer.sublime-settings'
SERVER_BINARY_PATH = '/live-server/live-server.js'
PLUGIN_NODE_PATH = os.path.join(
  os.path.dirname(os.path.realpath(__file__)),
  SERVER_BINARY_PATH
)

SERVER_PROCESS = None

class LiveServerStartCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    global SERVER_PROCESS
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

    self.view.window().status_message('🎉 Live Server running on {}.'.format(settings.get('port')))
    self.view.set_status('live_server_status', 'Live Server ✔️')