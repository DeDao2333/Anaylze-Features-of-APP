
from mxnet import nd

# 全部的危险权限列表
DANGER_PERMISSION = ['READ_CALENDAR', 'WRITE_CALENDAR',
                     'CAMERA'
                     'READ_CONTACTS', 'WRITE_CONTACTS', 'GET_ACCOUNTS',
                     'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION',
                     'RECORD_AUDIO',
                     'READ_PHONE_STATE', 'CALL_PHONE', 'READ_CALL_LOG', 'WRITE_CALL_LOG', 'ADD_VOICEMAIL', 'USE_SIP',
                     'PROCESS_OUTGOING_CALLS',
                     'BODY_SENSORS',
                     'SEND_SMS', 'RECEIVE_SMS', 'READ_SMS', 'RECEIVE_WAP_PUSH', 'RECEIVE_MMS',
                     'READ_EXTERNAL_STORAGE', 'WRITE_EXTERNAL_STORAGE']

# 商品类别
APK_CATEGORY = ['GAME', 'VIDEO', 'MUSIC', 'SOCIAL',
                'SHOPPING', 'LEARN', 'TRAVEL', 'READING']


def P2F_all(mes):
    '''
    将所有的apk的信息转换成特征和标签
    feature: 对应0/1——即在DANGER_PERMISSION相应位置上有没有信息
    label: 类别，可以类似于手写识别那一种，每一类对应一个数字 ## 未完成

    :param mes: 由Message类返回的对象
    :return: features, labels
    '''
    features = []
    labels = []
    allPermis = mes.getAllApks_Permission()

    for one in allPermis:
        labels.append(one)
        features.append(P2F_one(allPermis[one]))

    return features, labels


def P2F_one(permis):
    feature = nd.zeros((len(DANGER_PERMISSION),))

    for i in range(len(DANGER_PERMISSION)):
        for j in range(len(permis)):
            if permis[j] == DANGER_PERMISSION[i]:
                feature[i] = 1
    return feature

# test = ['READ_CALENDAR', 'WRITE_CALENDAR',
#                      'CAMERA'
#                      'READ_CONTACTS', 'WRITE_CONTACTS', 'GET_ACCOUNTS',
#                      'ACCESS_FINE_LOCATION', 'ACCESS_COARSE_LOCATION']
#
#
# print(P2F_one(test))
