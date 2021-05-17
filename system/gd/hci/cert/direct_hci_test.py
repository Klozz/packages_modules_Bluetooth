#!/usr/bin/env python3
#
#   Copyright 2019 - The Android Open Source Project
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from cert.gd_base_test import GdBaseTestClass
from hci.cert.direct_hci_test_lib import DirectHciTestBase


class DirectHciTest(GdBaseTestClass, DirectHciTestBase):

    def setup_class(self):
        GdBaseTestClass.setup_class(self, dut_module='HCI', cert_module='HAL')

    def setup_test(self):
        GdBaseTestClass.setup_test(self)
        DirectHciTestBase.setup_test(self, self.dut, self.cert)

    def teardown_test(self):
        DirectHciTestBase.teardown_test(self)
        GdBaseTestClass.teardown_test(self)
