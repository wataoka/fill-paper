import os
import sys
import json
import argparse

import pandas as pd

from src.utils.google_sheet import get_sheet
from src.utils.scraping import get_authors, get_date, get_title


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sheetname',
                        type=str, default='2021年',
                        help='name of sheet you access')
    args = parser.parse_args()
    return args


def main():

    args = parse_args()

    print('loading google sheet...')
    sheet = get_sheet(args.sheetname)
    sheet_df = pd.DataFrame(sheet.get_all_records())

    arxiv_bools = sheet_df['リンク'].str.contains('arxiv')

    col_names = ['論文名', '投稿日付', '著者']
    for col_name in col_names:
        empty_bools = sheet_df[col_name].str.len() == 0
        target_rows = sheet_df[arxiv_bools & empty_bools]
        for i in range(len(target_rows)):
            arxiv_url = target_rows.iloc[i]['リンク']

            value = None
            if col_name == '論文名':
                value = get_title(arxiv_url)
            elif col_name == '投稿日付':
                value = get_date(arxiv_url)
            elif col_name == '著者':
                value = get_authors(arxiv_url)
            else:
                continue

            col_name2idx = {'論文名': 'B', '投稿日付': 'D', '著者': 'E'}
            col_idx = col_name2idx[col_name]
            row_idx = str(target_rows.index[i] + 2)
            cell_idx = col_idx + row_idx

            if value is not None:
                sheet.update(cell_idx, value)


if __name__ == "__main__":
    main()
