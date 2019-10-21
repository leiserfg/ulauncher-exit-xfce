from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.SmallResultItem import SmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import (
    RenderResultListAction
)
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from ulauncher.utils.image_loader import icon_theme, Gtk
 
def get_icon_path(name, size):
    info = icon_theme.lookup_icon(name, size, Gtk.IconLookupFlags.FORCE_SIZE)
    if info is not None:
        return info.get_filename()

def create_item(name, icon, keyword, description, on_enter):
    return (
        keyword,
        ExtensionResultItem(
            name=name,
            description=description,
            icon=get_icon_path(icon, ExtensionResultItem.ICON_SIZE),
            on_enter=RunScriptAction('xfce4-session-logout --{}'.format(on_enter), None),
        )
    )

class XFCESessionExtension(Extension):
    def __init__(self):
        super(XFCESessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


items_cache = [
    create_item('Logout', 'xfsm-logout', 'logout', 'Session logout', 'logout'),
    create_item('Reboot', 'xfsm-reboot', 'reboot', 'Reboot computer', 'reboot'),
    create_item('Shutdown', 'xfsm-shutdown', 'shutdown', 'Shutdown computer', 'halt'),
    create_item('Suspend', 'xfsm-suspend', 'suspend', 'Suspend computer', 'suspend'),
    create_item('Hibernate', 'xfsm-hibernate', 'hibernate', 'Hibernate computer', 'hibernate'),
]


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        term = (event.get_argument() or '').lower()
        items = [i for name, i in items_cache if name.startswith(term)]
        return RenderResultListAction(items)


if __name__ == '__main__':
    XFCESessionExtension().run()
