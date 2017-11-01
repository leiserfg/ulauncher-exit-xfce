from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import (
    RenderResultListAction
)
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


class XFCESessionExtension(Extension):
    def __init__(self):
        super(XFCESessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


items_cache = [
    ("reboot", ExtensionResultItem(
        icon='images/reboot.png',
        name='Reboot',
        description='Reboot computer',
        on_enter=RunScriptAction("xfce4-session-logout --reboot", None))),
    ("shutdown", ExtensionResultItem(
                                 icon='images/shutdown.png',
                                 name='Shutdown',
                                 description='Power off computer',
                                 on_enter=RunScriptAction(
                                     "xfce4-session-logout --halt", None))),
    ("logout", ExtensionResultItem(
        icon='images/logout.png',
        name='Logout',
        description='Logout from session',
        on_enter=RunScriptAction("xfce4-session-logout --logout", None)))
]


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):

        term = (event.get_argument() or "").lower()
        items = [i for name, i in items_cache if name.startswith(term)]
        return RenderResultListAction(items)


if __name__ == '__main__':
    XFCESessionExtension().run()
