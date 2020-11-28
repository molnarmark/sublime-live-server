import sublime
import sublime_plugin
import subprocess
import os

SETTINGS_FILE = 'LiveServer.sublime-settings'
SERVER_BINARY_PATH = '/usr/local/lib/node_modules/live-server/live-server.js'
PLUGIN_NODE_PATH = os.path.join(
  os.path.dirname(os.path.realpath(__file__)),
  SERVER_BINARY_PATH
)

SERVER_PROCESS = None

class LiveServerStartCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    global SERVER_PROCESS
    settings = sublime.load_settings(SETTINGS_FILE)
    project_path = self.view.window().project_data()['folders'][0]['path']
    SERVER_PROCESS = subprocess.Popen(
      ["/usr/bin/node", PLUGIN_NODE_PATH, project_path],
      stdout=subprocess.PIPE,
      stdin=subprocess.PIPE,
      stderr=subprocess.PIPE,
      env=os.environ.copy(),
      startupinfo=None,
    )

    self.view.window().status_message('🌎 Live Server running on {}.'.format(settings.get('port')))
    self.view.set_status('live_server_status', 'Live Server ✔️')


class LiveServerStopCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    SERVER_PROCESS.terminate()
    self.view.window().status_message('❌ Live Server stopped.')
    self.view.erase_status('live_server_status')