# coding: utf-8

"""
    Criação de Contas

    API de Criação de Contas.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: cadastro_api@orama.com.br
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DocumentoCorpo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'filename': 'file'
    }

    attribute_map = {
        'name': 'name',
        'filename': 'filename'
    }

    def __init__(self, name=None, filename=None):  # noqa: E501
        """DocumentoCorpo - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._filename = None
        self.discriminator = None

        self.name = name
        self.filename = filename

    @property
    def name(self):
        """Gets the name of this DocumentoCorpo.  # noqa: E501

        Nome do atributo codificado em form-data 'image'  # noqa: E501

        :return: The name of this DocumentoCorpo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentoCorpo.

        Nome do atributo codificado em form-data 'image'  # noqa: E501

        :param name: The name of this DocumentoCorpo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def filename(self):
        """Gets the filename of this DocumentoCorpo.  # noqa: E501

        Arquivo binário que será enviado. O formato deve ser PDF, PNG ou JPG  # noqa: E501

        :return: The filename of this DocumentoCorpo.  # noqa: E501
        :rtype: file
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this DocumentoCorpo.

        Arquivo binário que será enviado. O formato deve ser PDF, PNG ou JPG  # noqa: E501

        :param filename: The filename of this DocumentoCorpo.  # noqa: E501
        :type: file
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DocumentoCorpo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
