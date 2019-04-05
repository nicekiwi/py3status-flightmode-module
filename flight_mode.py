# -*- coding: utf-8 -*-
"""
Display text "FM" when the Wifi radio is turned off.

Requires "nmcli".
"""


class Py3status:

    cache_timeout = 10
    format = '[\?if=status=disabled&color=good FM]'
    
    def flight_mode(self):
    	return {
            'full_text': self.py3.safe_format(self.format, { "status": self._check_radio_status() }),
            'cached_until': self.py3.time_in(self.cache_timeout)
        }


    def _check_radio_status(self):
        return self.py3.command_output("nmcli radio wifi").strip('\n')

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)
