class TextLibrary:
    '''文本库，用于管理要显示的文本'''
    def __init__(self):
        self.info_texts = {
            'welcome': '恭喜您收到了我们的博士录取通知书！您愿意来我们学院读博吗？',
            'reject': '你仔细想了想，决定不读博了。可能在这个世界线里，这是一个更好的选择'
        }

    def get_text(self, key):
        '''根据key获取文本'''
        return self.info_texts.get(key, 'Unknown text key')    