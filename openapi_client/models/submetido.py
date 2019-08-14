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


class Submetido(object):
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
        'submetido': 'bool'
    }

    attribute_map = {
        'submetido': 'submetido'
    }

    def __init__(self, submetido=None):  # noqa: E501
        """Submetido - a model defined in OpenAPI"""  # noqa: E501

        self._submetido = None
        self.discriminator = None

        if submetido is not None:
            self.submetido = submetido

    @property
    def submetido(self):
        """Gets the submetido of this Submetido.  # noqa: E501

        Estado de submissão do perfil, true caso já tenha sido submetido, false caso contrário.  # noqa: E501

        :return: The submetido of this Submetido.  # noqa: E501
        :rtype: bool
        """
        return self._submetido

    @submetido.setter
    def submetido(self, submetido):
        """Sets the submetido of this Submetido.

        Estado de submissão do perfil, true caso já tenha sido submetido, false caso contrário.  # noqa: E501

        :param submetido: The submetido of this Submetido.  # noqa: E501
        :type: bool
        """

        self._submetido = submetido

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
        if not isinstance(other, Submetido):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
