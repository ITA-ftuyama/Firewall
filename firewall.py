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
            'type': data[1],
            'kind': data[2]
        }
        for key in ['src', 'dst']:
            if key in data:
                rule[key] = data[data.index(key) + 1]
                if data[2] == 'TCP':
                    rule[key] = int(rule[key])
        return rule

    def read_rules(self, file_name):
        u"""Lê o arquivo de regras do Firewall."""
        self.rules = []
        with open(file_name, 'r') as file:
            for line in file:
                self.rules.append(
                    self.create_rule(line.split()))
        print self.rules
