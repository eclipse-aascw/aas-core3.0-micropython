# SPDX-FileCopyrightText: 2023 aas-core3.0-python AUTHORS
# SPDX-FileCopyrightText: 2023 aas-core3.0-micropython AUTHORS
#
# SPDX-License-Identifier: MIT


def assert_never(value):

    assert False, f"Unhandled value: {value} ({type(value).__name__})"
