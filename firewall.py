# -*- coding: utf-8 -*-
# !/usr/bin/env python
u"""Módulo Firewall para SDN."""


class Firewall:
    u"""Firewall básico."""

    def __init__(self):
        u"""Inicializa o Firewall."""
        self.read_rules("rules.txt")

    def create_rule(self, data):
        u"""Cria regra a partir da linha."""
        rule = {
            'n': data[0],
            'kind': data[2]
        }
        if 'src' in data:
            rule['src'] = data[data.index('src') + 1]
            if data[2] == 'TCP':
                rule['src'] = int(rule['src'])
        if 'dst' in data:
            rule['dst'] = data[data.index('dst') + 1]
            if data[2] == 'TCP':
                rule['dst'] = int(rule['dst'])
        return rule

    def read_rules(self, file_name):
        u"""Lê o arquivo de regras do Firewall."""
        self.rules = {
            'permit': [],
            'deny': []
        }
        with open(file_name, 'r') as file:
            for line in file:
                data = line.split()
                self.rules[data[1]].append(
                    self.create_rule(data))
        print self.rules
