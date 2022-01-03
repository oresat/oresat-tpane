#!/usr/bin/env python3
from urwid import MainLoop, \
                  Padding, \
                  LineBox, \
                  Filler, \
                  Edit, \
                  Text, \
                  Widget, \
                  RELATIVE_100


class InputBox(Filler):
    def __init__(self, banner_txt: str):
        super().__init__(self.__set_body(Edit(banner_txt)), top=0)


    @property
    def body(self):
        return super().body.original_widget.original_widget

    def __set_body(self, widget: Widget):
        self._sizing
        self.original_widget = Padding(LineBox(widget), align='center', left=0, width=RELATIVE_100)
        return self.original_widget

    def keypress(self, size, key):
        if(key != 'enter'):
            return super(InputBox, self).keypress(size, key)
        greeting_box = Text(f'Why hello there, {self.body.edit_text}')
        self.__set_body(greeting_box)



def cmd_handler(cmd):
    print(cmd)


def main():
    event_loop = MainLoop(InputBox('What\'s yer name, son?: '))

    try:
        event_loop.run()
    except KeyboardInterrupt:
        print('Goodbye!')


if __name__ == '__main__':
    main()
