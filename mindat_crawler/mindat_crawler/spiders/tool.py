class Tools():
    @staticmethod
    def get_search_url(keyword):
        return 'https://www.mindat.org/photoscroll.php?frm_id=pscroll&cform_is_valid=1&searchbox={keyword}&submit_pscroll=Search'.format(keyword=keyword)


class MetaInfo():
    