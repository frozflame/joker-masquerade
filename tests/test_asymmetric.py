#!/usr/bin/env python3
# coding: utf-8

from joker.masquerade.rsa import RSAKeyPair


def test_rsa_key_pair():
    m = 'keep me as a secret'
    kpair = RSAKeyPair()
    cipher = kpair.encrypt(m.encode())
    assert kpair.decrypt(cipher) == m.encode()



