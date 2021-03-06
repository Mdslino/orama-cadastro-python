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


class UsuarioSenhaObjeto(object):
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
        'usuario': 'str',
        'senha': 'str'
    }

    attribute_map = {
        'usuario': 'usuario',
        'senha': 'senha'
    }

    def __init__(self, usuario=None, senha=None):  # noqa: E501
        """UsuarioSenhaObjeto - a model defined in OpenAPI"""  # noqa: E501

        self._usuario = None
        self._senha = None
        self.discriminator = None

        self.usuario = usuario
        self.senha = senha

    @property
    def usuario(self):
        """Gets the usuario of this UsuarioSenhaObjeto.  # noqa: E501

        Identificador do usuário, CPF ou email  # noqa: E501

        :return: The usuario of this UsuarioSenhaObjeto.  # noqa: E501
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        """Sets the usuario of this UsuarioSenhaObjeto.

        Identificador do usuário, CPF ou email  # noqa: E501

        :param usuario: The usuario of this UsuarioSenhaObjeto.  # noqa: E501
        :type: str
        """
        if usuario is None:
            raise ValueError("Invalid value for `usuario`, must not be `None`")  # noqa: E501

        self._usuario = usuario

    @property
    def senha(self):
        """Gets the senha of this UsuarioSenhaObjeto.  # noqa: E501

        Senha de seis dígitos.  # noqa: E501

        :return: The senha of this UsuarioSenhaObjeto.  # noqa: E501
        :rtype: str
        """
        return self._senha

    @senha.setter
    def senha(self, senha):
        """Sets the senha of this UsuarioSenhaObjeto.

        Senha de seis dígitos.  # noqa: E501

        :param senha: The senha of this UsuarioSenhaObjeto.  # noqa: E501
        :type: str
        """
        if senha is None:
            raise ValueError("Invalid value for `senha`, must not be `None`")  # noqa: E501
        if senha is not None and not re.search(r'^\d{6}$', senha):  # noqa: E501
            raise ValueError(r"Invalid value for `senha`, must be a follow pattern or equal to `/^\d{6}$/`")  # noqa: E501

        self._senha = senha

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
        if not isinstance(other, UsuarioSenhaObjeto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
