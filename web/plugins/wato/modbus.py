#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# cmk_modbus - Check_MK plugin to poll data from modbus-enabled modbus_devices
#
# Authors:
#   Mathias Krüger <noreply@ibh.de>
#
# Copyright Holder:
#   2016 (C) IBH IT-Service GmbH [http://www.ibh.de/]
#
# License:
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this package; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
#

group = "datasource_programs"

register_rule(group,
    "special_agents:modbus",
     Dictionary(
        title = _("Check state of Modbus TCP Devices"),
        help = _( "Configure address, tcp-port and type of device according to the supported devices. "
                  "New devices can be added, by dropping a json file into the special_agent/modbus_devices folder."),
        elements = [
            ( "port",
              Integer(
                  title = _("Port"),
                  default_value = 502,
                  minvalue = 1,
              )
            ),
            ( "dev",
              TextAscii(
                  title = _("Device Type"),
              )
            ),
        ],
        optional_keys = [ "port" ],
    ),
    factory_default = FACTORY_DEFAULT_UNUSED, # No default, do not use setting if no rule matches
    match = 'first')
