import sublime, sublime_plugin

class HaskellErrorChecker(sublime_plugin.EventListener):
    def on_post_save(self, view):
        syntax_file_for_view = view.settings().get('syntax').lower()
        is_haskell_file = 'haskell' in syntax_file_for_view
        if is_haskell_file:
            self.write_output(view, 'Your program has lots of errors!')

    def write_output(self, view, text):
        PANEL_NAME = 'haskell_error_checker'
        output_view = view.window().get_output_panel(PANEL_NAME)
        edit = output_view.begin_edit()
        output_view.insert(edit, 0, 'You have errors in your program!')
        output_view.end_edit(edit)
        view.window().run_command('show_panel', {'panel': 'output.' + PANEL_NAME})
