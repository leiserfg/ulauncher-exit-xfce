from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
import os

class CinnamonSessionExtension(Extension):

    def __init__(self):
        super(CinnamonSessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
    	options = ['logout', 'restart', 'reboot', 'shutdown', 'halt']
        myList = event.query.split(" ")
        if len(myList) == 1:
            items.append(ExtensionResultItem(icon='images/reboot.png',
                                            name='Reboot',
                                            description='Reboot computer',
                                            on_enter=RunScriptAction("cinnamon-session-quit --reboot", None)))
            items.append(ExtensionResultItem(icon='images/shutdown.png',
                                            name='Shutdown',
                                            description='Power off computer',
                                            on_enter=RunScriptAction("cinnamon-session-quit --power-off", None)))
            items.append(ExtensionResultItem(icon='images/logout.png',
                                            name='Logout',
                                            description='Logout from session',
                                            on_enter=RunScriptAction("cinnamon-session-quit --logout", None)))

            return RenderResultListAction(items)
        else:
            myQuery = myList[1]
            included = []
            for option in options:
                if myQuery in option:
                    if option in ['shutdown', 'halt'] and 'shutdown' not in included:
                        items.append(ExtensionResultItem(icon='images/shutdown.png',
                                                        name='Shutdown',
                                                        description='Power off computer',
                                                        on_enter=RunScriptAction("cinnamon-session-quit --power-off", None)))
                        included.append('shutdown')
                    elif option in ['restart', 'reboot'] and 'reboot' not in included:
                        items.append(ExtensionResultItem(icon='images/reboot.png',
                                                    name='Reboot',
                                                    description='Reboot computer',
                                                    on_enter=RunScriptAction("cinnamon-session-quit --reboot", None)))
                        included.append('reboot')
                    elif option in ['logout']:
                        items.append(ExtensionResultItem(icon='images/logout.png',
                                                    name='Logout',
                                                    description='Logout from session',
                                                    on_enter=RunScriptAction("cinnamon-session-quit --logout", None)))

            return RenderResultListAction(items)

if __name__ == '__main__':
    CinnamonSessionExtension().run()
