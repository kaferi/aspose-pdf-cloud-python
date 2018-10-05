# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2018 Aspose.PDF Cloud
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.



    OpenAPI spec version: 2.0
    
"""


from pprint import pformat
from six import iteritems
import re


class ImageTemplatesRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_ocr': 'bool',
        'ocr_langs': 'str',
        'images_list': 'list[ImageTemplate]'
    }

    attribute_map = {
        'is_ocr': 'IsOCR',
        'ocr_langs': 'OCRLangs',
        'images_list': 'ImagesList'
    }

    def __init__(self, is_ocr=None, ocr_langs=None, images_list=None):
        """
        ImageTemplatesRequest - a model defined in Swagger
        """

        self._is_ocr = None
        self._ocr_langs = None
        self._images_list = None

        self.is_ocr = is_ocr
        if ocr_langs is not None:
          self.ocr_langs = ocr_langs
        self.images_list = images_list

    @property
    def is_ocr(self):
        """
        Gets the is_ocr of this ImageTemplatesRequest.
        Using OCR function.

        :return: The is_ocr of this ImageTemplatesRequest.
        :rtype: bool
        """
        return self._is_ocr

    @is_ocr.setter
    def is_ocr(self, is_ocr):
        """
        Sets the is_ocr of this ImageTemplatesRequest.
        Using OCR function.

        :param is_ocr: The is_ocr of this ImageTemplatesRequest.
        :type: bool
        """
        if is_ocr is None:
            raise ValueError("Invalid value for `is_ocr`, must not be `None`")

        self._is_ocr = is_ocr

    @property
    def ocr_langs(self):
        """
        Gets the ocr_langs of this ImageTemplatesRequest.
        Language for recognition possible values: eng, ara, bel, ben, bul, ces, dan, deu, ell, fin, fra, heb, hin, ind, isl, ita, jpn, kor, nld, nor, pol, por, ron, rus, spa, swe, tha, tur, ukr, vie, chi_sim, chi_tra      or thier combination e.g. eng+rus

        :return: The ocr_langs of this ImageTemplatesRequest.
        :rtype: str
        """
        return self._ocr_langs

    @ocr_langs.setter
    def ocr_langs(self, ocr_langs):
        """
        Sets the ocr_langs of this ImageTemplatesRequest.
        Language for recognition possible values: eng, ara, bel, ben, bul, ces, dan, deu, ell, fin, fra, heb, hin, ind, isl, ita, jpn, kor, nld, nor, pol, por, ron, rus, spa, swe, tha, tur, ukr, vie, chi_sim, chi_tra      or thier combination e.g. eng+rus

        :param ocr_langs: The ocr_langs of this ImageTemplatesRequest.
        :type: str
        """

        self._ocr_langs = ocr_langs

    @property
    def images_list(self):
        """
        Gets the images_list of this ImageTemplatesRequest.
        A List of objects describing images to be added.

        :return: The images_list of this ImageTemplatesRequest.
        :rtype: list[ImageTemplate]
        """
        return self._images_list

    @images_list.setter
    def images_list(self, images_list):
        """
        Sets the images_list of this ImageTemplatesRequest.
        A List of objects describing images to be added.

        :param images_list: The images_list of this ImageTemplatesRequest.
        :type: list[ImageTemplate]
        """
        if images_list is None:
            raise ValueError("Invalid value for `images_list`, must not be `None`")

        self._images_list = images_list

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ImageTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other