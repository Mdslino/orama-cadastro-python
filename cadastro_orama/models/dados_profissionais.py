# coding: utf-8

"""
    Criação de Contas

    API de Criação de Contas.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: cadastro_api@orama.com.br
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cadastro_orama.configuration import Configuration


class DadosProfissionais(object):
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
        'profissao': 'str',
        'empresa': 'str'
    }

    attribute_map = {
        'profissao': 'profissao',
        'empresa': 'empresa'
    }

    def __init__(self, profissao=None, empresa=None, local_vars_configuration=None):  # noqa: E501
        """DadosProfissionais - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._profissao = None
        self._empresa = None
        self.discriminator = None

        if profissao is not None:
            self.profissao = profissao
        if empresa is not None:
            self.empresa = empresa

    @property
    def profissao(self):
        """Gets the profissao of this DadosProfissionais.  # noqa: E501

        Profissão de acordo com a tabela de ocupação profissional  # noqa: E501

        :return: The profissao of this DadosProfissionais.  # noqa: E501
        :rtype: str
        """
        return self._profissao

    @profissao.setter
    def profissao(self, profissao):
        """Sets the profissao of this DadosProfissionais.

        Profissão de acordo com a tabela de ocupação profissional  # noqa: E501

        :param profissao: The profissao of this DadosProfissionais.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                profissao is not None and len(profissao) > 200):
            raise ValueError("Invalid value for `profissao`, length must be less than or equal to `200`")  # noqa: E501

        self._profissao = profissao

    @property
    def empresa(self):
        """Gets the empresa of this DadosProfissionais.  # noqa: E501

        Nome da empresa em que trabalha o usuário  # noqa: E501

        :return: The empresa of this DadosProfissionais.  # noqa: E501
        :rtype: str
        """
        return self._empresa

    @empresa.setter
    def empresa(self, empresa):
        """Sets the empresa of this DadosProfissionais.

        Nome da empresa em que trabalha o usuário  # noqa: E501

        :param empresa: The empresa of this DadosProfissionais.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                empresa is not None and len(empresa) > 50):
            raise ValueError("Invalid value for `empresa`, length must be less than or equal to `50`")  # noqa: E501

        self._empresa = empresa

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
        if not isinstance(other, DadosProfissionais):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DadosProfissionais):
            return True

        return self.to_dict() != other.to_dict()
