# -*- coding: utf-8 -*-
import pytest

from validators import hostname, ValidationFailure


@pytest.mark.parametrize('value', [
    '01010',
    'A0c-',
    '-A0c',
    'o123456701234567012345670123456701234567012345670123456701234567',
    'example.com/',
    'example.com:4444',
    'example.-com',
    '-example.com',
    '!example.com',
    '123123123.example.com'])
def test_returns_false_on_invalid_hostname(value):
    assert isinstance(hostname(value), ValidationFailure)


@pytest.mark.parametrize('value', [
    'abc',
    'A0c',
    'A-0c',
    'o12345670123456701234567012345670123456701234567012345670123456',
    'a',
    '0--0'])
def test_returns_true_on_valid_hostname(value):
    assert hostname(value)


@pytest.mark.parametrize('value', [
    'www',
    'example.com',
    'xn----gtbspbbmkef.xn--p1ai',
    'underscore_subdomain.example.com',
    'something.versicherung',
    'example.com.',
    '_srv._xmpp-server._tcp.example.com.',
    '_srv._xmpp-server._tcp',

])
def test_returns_true_on_valid_domain(value):
    assert hostname(value)
