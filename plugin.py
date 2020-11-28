import sublime
import sublime_plugin

SETTINGS_FILE = 'LiveServer.sublime-settings'

class LiveServerStartCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = sublime.load_settings(SETTINGS_FILE)
    self.view.window().status_message('🌎 Live Server running on {}.'.format(settings.get('port')))


class LiveServerStopCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().status_message('❌ Live Server stopped.')