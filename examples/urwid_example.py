#!/usr/bin/env python3
from urwid import MainLoop, \
                  Filler, \
                  Edit, \
                  Text, \
                  Terminal


class InputBox(Filler):
    def __init__(self, banner_txt: str):
        super().__init__(Edit(banner_txt), 'middle')

    def keypress(self, size, key):
        if(key != 'enter'):
            return super(InputBox, self).keypress(size, key)
        self.original_widget = Text(f'Why hello there, {self.body.edit_text}')



def cmd_handler(cmd):
    print(cmd)


def main():
    term = Terminal(cmd_handler)
    event_loop = MainLoop(term)

    try:
        event_loop.run()
    except KeyboardInterrupt:
        print('Goodbye!')


if __name__ == '__main__':
    main()
