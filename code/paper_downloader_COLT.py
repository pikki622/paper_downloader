"""paper_downloader_COLT.py"""
import lib.pmlr as pmlr


def download_paper(year, save_dir, is_download_supplement=True, time_step_in_seconds=5, downloader='IDM'):
    """
    download all COLT paper and supplement files given year, restore in save_dir/main_paper and save_dir/supplement
    respectively
    :param year: int, COLT year, such as 2019
    :param save_dir: str, paper and supplement material's save path
    :param is_download_supplement: bool, True for downloading supplemental material
    :param time_step_in_seconds: int, the interval time between two downlaod request in seconds
    :param downloader: str, the downloader to download, could be 'IDM' or 'Thunder', default to 'IDM'
    :return: True
    """
    COLT_year_dict = {2020: 125,
                      2019: 99,
                      2018: 75,
                      2017: 65,
                      2016: 49,
                      2015: 40,
                      2014: 35,
                      2013: 30,
                      2012: 23,
                      2011: 19
                      }
    if year in COLT_year_dict.keys():
        volume = f'v{COLT_year_dict[year]}'
    else:
        raise ValueError('''the given year's url is unknown !''')
    postfix = f'COLT_{year}'

    pmlr.download_paper_given_volume(
        volume=volume,
        save_dir=save_dir,
        postfix=postfix,
        is_download_supplement=is_download_supplement,
        time_step_in_seconds=time_step_in_seconds,
        downloader=downloader
    )


if __name__ == '__main__':
    year = 2011
    download_paper(
        year,
        rf'D:\COLT_{year}',
        is_download_supplement=True,
        time_step_in_seconds=5,
        downloader='IDM'
    )
    pass