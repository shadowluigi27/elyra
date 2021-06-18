#
# Copyright 2018-2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class TestOperator(BaseOperator):
    r"""
    Execute a test script.

    :param test_string_no_default: The test command description
    :type test_string_no_default: str
    :param test_bool_default: The test command bool description
    :type test_bool_default: bool
    :param test_int_default: The test command int description
    :type test_int_default: int
    :param test_string_default_value: The test command description
    :type test_string_default_value: str
    :param test_string_default_empty: The test command description
    :type test_string_default_empty: str
    :param test_bool_false: The test command bool description
    :type test_bool_false: bool
    :param test_bool_true: The test command bool description
    :type test_bool_true: bool
    :param test_int_zero: The test command int description
    :type test_int_zero: int
    :param test_int_non_zero: The test command int description
    :type test_int_non_zero: int
    """

    @apply_defaults
    def __init__(self,
                 test_string_no_default,
                 test_bool_default,
                 test_int_default,
                 test_string_default_value='default',
                 test_string_default_empty=None,
                 test_bool_false=False,
                 test_bool_true=True,
                 test_int_zero=0,
                 test_int_non_zero=1,
                 *args, **kwargs):

        super(TestOperator, self).__init__(*args, **kwargs)
