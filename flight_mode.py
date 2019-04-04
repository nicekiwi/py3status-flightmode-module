# -*- coding: utf-8 -*-
"""
Example module that says 'Hello World!'

This demonstrates how to produce a simple custom module.
"""


class Py3status:

    cache_timeout = 1
    format = '[\?if=status&color=good FM]'
    
    def flight_mode(self):
    	result = {}
    	if self._check_radio_status() == "disabled":
    	    result["status"] = "disabled"
    	return {
            'full_text': self.py3.safe_format(self.format, result),
            'cached_until': self.py3.time_in(self.cache_timeout)
        }


    def _check_radio_status(self):
        return self.py3.command_output("nmcli radio wifi")

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)
