# -*- coding: utf-8 -*-
import os
import sys
import zipfile
import re


class Message:

    def __init__(self, path):
        self.dir_path = path
        self.allApk_permis = {}

    def getPermission(self, apk_path):
        """
        获取指定apk的权限
        :param apk_path: 这里是apk的绝对路径
        :return: 字典，{'知乎'：Permissions_list}
        """
        pp = os.popen("aapt d permissions " + apk_path)
        pp = pp.readlines()
        permission_list = self.__dealWith_PermissionList(pp)  # 抽取出权限名称
        name = self.__getName(apk_path)  # 从路径中抽取出名称
        temp = {name: permission_list}
        return temp

    def getAllApks_Permission(self):
        """
        获取全部apk名称加权限
        :return: 字典，like { ’知乎‘ ：Permission_list, '淘宝' : ...}
        """
        apks_path = self.getAllPath(self.dir_path)

        for path in apks_path:
            message = self.getPermission(path)
            self.allApk_permis.update(message)

        return self.allApk_permis

    def getAllPath(self, dirPath):
        """
        获取全部apk的绝对路径
        :param dirPath:
        :return:
        """
        all_names = []
        all_paths = []
        for _, _, files in os.walk(dirPath):
            all_names[:] = files[:]
        for name in all_names:
            all_paths.append(self.__getAbsPath(dirPath, name))
        return all_paths

    def __getName(self, absPath):
        """
        从绝对路径中抽取出apk名称
        :param absPath:
        :return: ‘知乎’
        """
        return absPath.split('\\')[-1].split('.')[0]

    def __getAbsPath(self, dirPath, name):
        return os.path.join(dirPath, name)

    @staticmethod
    def __dealWith_PermissionList(permissions):
        """
        处理得到的raw权限列表，从中抽取出权限名称
        :return:
        """
        permissions_names = []
        permissions[:] = permissions[1:]
        for per in permissions:
            str = per.split('\'')
            if len(str) >= 2:
                sub_per = str[1].split('.')
                if len(sub_per) == 3:
                    permissions_names.append(sub_per[-1])

        return permissions_names


