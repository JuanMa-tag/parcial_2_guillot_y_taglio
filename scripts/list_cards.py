#!/usr/bin/env python3
import csv
import argparse
import os

BASE = os.path.dirname(os.path.dirname(__file__))

FILES = {
    'terrestres': os.path.join(BASE, 'terrestres.csv'),
    'aereos': os.path.join(BASE, 'aereos.csv'),
    'hechizos': os.path.join(BASE, 'hechizos.csv'),
}


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def filter_cards(cards, min_elixir, max_elixir, rareza):
    out = []
    for c in cards:
        try:
            el = int(c.get('elixir', '') or 0)
        except ValueError:
            el = 0
        r = c.get('rareza', '')
        if min_elixir is not None and el < min_elixir:
            continue
        if max_elixir is not None and el > max_elixir:
            continue
        if rareza and r.lower() != rareza.lower():
            continue
        out.append((c.get('nombre', ''), el, r))
    return out


def main():
    p = argparse.ArgumentParser(description='List and filter Clash Royale cards from CSVs')
    p.add_argument('--subcategoria', choices=FILES.keys(), required=True)
    p.add_argument('--min-elixir', type=int, default=None)
    p.add_argument('--max-elixir', type=int, default=None)
    p.add_argument('--rareza', type=str, default=None)
    args = p.parse_args()

    path = FILES[args.subcategoria]
    if not os.path.exists(path):
        print(f"No se encontró {path}")
        return

    cards = read_csv(path)
    results = filter_cards(cards, args.min_elixir, args.max_elixir, args.rareza)

    if not results:
        print('No se encontraron cartas con esos filtros.')
        return

    print(f"Cartas en {args.subcategoria} (nombre - elixir - rareza):")
    for name, el, r in results:
        print(f"- {name} — {el} elixir — {r}")


if __name__ == '__main__':
    main()
