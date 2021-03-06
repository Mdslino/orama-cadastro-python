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


class PerfilUsuario(object):
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
        'us_person': 'bool',
        'politicamente_exposto': 'bool',
        'investidor_qualificado': 'bool',
        'nacionalidade': 'str',
        'uf_nascimento': 'str',
        'cidade_nascimento': 'str',
        'pais_nascimento': 'str',
        'sexo': 'str',
        'estado_civil': 'str',
        'nome_conjuge': 'str',
        'nome_mae': 'str',
        'nome_pai': 'str',
        'login': 'LoginObjeto',
        'documento': 'list[Documento]',
        'profissao': 'DadosProfissionais',
        'endereco': 'Endereco',
        'patrimonio': 'DadosPatrimonial',
        'conta_bancaria': 'list[ContaBancaria]',
        'front_end': 'FrontEndStep'
    }

    attribute_map = {
        'us_person': 'usPerson',
        'politicamente_exposto': 'politicamenteExposto',
        'investidor_qualificado': 'investidorQualificado',
        'nacionalidade': 'nacionalidade',
        'uf_nascimento': 'ufNascimento',
        'cidade_nascimento': 'cidadeNascimento',
        'pais_nascimento': 'paisNascimento',
        'sexo': 'sexo',
        'estado_civil': 'estadoCivil',
        'nome_conjuge': 'nomeConjuge',
        'nome_mae': 'nomeMae',
        'nome_pai': 'nomePai',
        'login': 'login',
        'documento': 'documento',
        'profissao': 'profissao',
        'endereco': 'endereco',
        'patrimonio': 'patrimonio',
        'conta_bancaria': 'contaBancaria',
        'front_end': 'frontEnd'
    }

    def __init__(self, us_person=False, politicamente_exposto=False, investidor_qualificado=False, nacionalidade=None, uf_nascimento=None, cidade_nascimento=None, pais_nascimento=None, sexo=None, estado_civil=None, nome_conjuge=None, nome_mae=None, nome_pai=None, login=None, documento=None, profissao=None, endereco=None, patrimonio=None, conta_bancaria=None, front_end=None, local_vars_configuration=None):  # noqa: E501
        """PerfilUsuario - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._us_person = None
        self._politicamente_exposto = None
        self._investidor_qualificado = None
        self._nacionalidade = None
        self._uf_nascimento = None
        self._cidade_nascimento = None
        self._pais_nascimento = None
        self._sexo = None
        self._estado_civil = None
        self._nome_conjuge = None
        self._nome_mae = None
        self._nome_pai = None
        self._login = None
        self._documento = None
        self._profissao = None
        self._endereco = None
        self._patrimonio = None
        self._conta_bancaria = None
        self._front_end = None
        self.discriminator = None

        if us_person is not None:
            self.us_person = us_person
        if politicamente_exposto is not None:
            self.politicamente_exposto = politicamente_exposto
        if investidor_qualificado is not None:
            self.investidor_qualificado = investidor_qualificado
        if nacionalidade is not None:
            self.nacionalidade = nacionalidade
        if uf_nascimento is not None:
            self.uf_nascimento = uf_nascimento
        if cidade_nascimento is not None:
            self.cidade_nascimento = cidade_nascimento
        if pais_nascimento is not None:
            self.pais_nascimento = pais_nascimento
        if sexo is not None:
            self.sexo = sexo
        if estado_civil is not None:
            self.estado_civil = estado_civil
        if nome_conjuge is not None:
            self.nome_conjuge = nome_conjuge
        self.nome_mae = nome_mae
        if nome_pai is not None:
            self.nome_pai = nome_pai
        if login is not None:
            self.login = login
        self.documento = documento
        if profissao is not None:
            self.profissao = profissao
        self.endereco = endereco
        if patrimonio is not None:
            self.patrimonio = patrimonio
        if conta_bancaria is not None:
            self.conta_bancaria = conta_bancaria
        if front_end is not None:
            self.front_end = front_end

    @property
    def us_person(self):
        """Gets the us_person of this PerfilUsuario.  # noqa: E501

        define se o usuário pode ou não ser enquadrado como US person de acordo com a definição da CVM  # noqa: E501

        :return: The us_person of this PerfilUsuario.  # noqa: E501
        :rtype: bool
        """
        return self._us_person

    @us_person.setter
    def us_person(self, us_person):
        """Sets the us_person of this PerfilUsuario.

        define se o usuário pode ou não ser enquadrado como US person de acordo com a definição da CVM  # noqa: E501

        :param us_person: The us_person of this PerfilUsuario.  # noqa: E501
        :type: bool
        """

        self._us_person = us_person

    @property
    def politicamente_exposto(self):
        """Gets the politicamente_exposto of this PerfilUsuario.  # noqa: E501

        define se o usuário pode ou não ser enquadrado como pessoa politicamente exposta de acordo com a definição da Deliberação Coremec nº 2, de 1º de dezembro de 2006  # noqa: E501

        :return: The politicamente_exposto of this PerfilUsuario.  # noqa: E501
        :rtype: bool
        """
        return self._politicamente_exposto

    @politicamente_exposto.setter
    def politicamente_exposto(self, politicamente_exposto):
        """Sets the politicamente_exposto of this PerfilUsuario.

        define se o usuário pode ou não ser enquadrado como pessoa politicamente exposta de acordo com a definição da Deliberação Coremec nº 2, de 1º de dezembro de 2006  # noqa: E501

        :param politicamente_exposto: The politicamente_exposto of this PerfilUsuario.  # noqa: E501
        :type: bool
        """

        self._politicamente_exposto = politicamente_exposto

    @property
    def investidor_qualificado(self):
        """Gets the investidor_qualificado of this PerfilUsuario.  # noqa: E501

        Define se o usuário é investidor qualifiquado. Investidor Qualificado - PF ou PJ que possuam investimentos financeiros em valor superior a 1 Milhão, Investidor aprovado em exame de qualificação técnica, e atestem por escrito sua condição de investidor qualificado. Investidores Profissionais, etc.  # noqa: E501

        :return: The investidor_qualificado of this PerfilUsuario.  # noqa: E501
        :rtype: bool
        """
        return self._investidor_qualificado

    @investidor_qualificado.setter
    def investidor_qualificado(self, investidor_qualificado):
        """Sets the investidor_qualificado of this PerfilUsuario.

        Define se o usuário é investidor qualifiquado. Investidor Qualificado - PF ou PJ que possuam investimentos financeiros em valor superior a 1 Milhão, Investidor aprovado em exame de qualificação técnica, e atestem por escrito sua condição de investidor qualificado. Investidores Profissionais, etc.  # noqa: E501

        :param investidor_qualificado: The investidor_qualificado of this PerfilUsuario.  # noqa: E501
        :type: bool
        """

        self._investidor_qualificado = investidor_qualificado

    @property
    def nacionalidade(self):
        """Gets the nacionalidade of this PerfilUsuario.  # noqa: E501

        Definição de Nacionalidade de acordo com o Art. 12 da CF  # noqa: E501

        :return: The nacionalidade of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        """Sets the nacionalidade of this PerfilUsuario.

        Definição de Nacionalidade de acordo com o Art. 12 da CF  # noqa: E501

        :param nacionalidade: The nacionalidade of this PerfilUsuario.  # noqa: E501
        :type: str
        """
        allowed_values = ["Brasileiro Nato", "Estrangeiro", "Brasileiro Naturalizado"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and nacionalidade not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `nacionalidade` ({0}), must be one of {1}"  # noqa: E501
                .format(nacionalidade, allowed_values)
            )

        self._nacionalidade = nacionalidade

    @property
    def uf_nascimento(self):
        """Gets the uf_nascimento of this PerfilUsuario.  # noqa: E501

        Unidade da Federação em que a pessoa nasceu  # noqa: E501

        :return: The uf_nascimento of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._uf_nascimento

    @uf_nascimento.setter
    def uf_nascimento(self, uf_nascimento):
        """Sets the uf_nascimento of this PerfilUsuario.

        Unidade da Federação em que a pessoa nasceu  # noqa: E501

        :param uf_nascimento: The uf_nascimento of this PerfilUsuario.  # noqa: E501
        :type: str
        """
        allowed_values = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and uf_nascimento not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `uf_nascimento` ({0}), must be one of {1}"  # noqa: E501
                .format(uf_nascimento, allowed_values)
            )

        self._uf_nascimento = uf_nascimento

    @property
    def cidade_nascimento(self):
        """Gets the cidade_nascimento of this PerfilUsuario.  # noqa: E501

        Município em que a pessoa nascida no Brasil nasceu. Formato é o nome lexicograficamente igual a descrição do IBGE ou o código de cidade completo do IBGE  # noqa: E501

        :return: The cidade_nascimento of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._cidade_nascimento

    @cidade_nascimento.setter
    def cidade_nascimento(self, cidade_nascimento):
        """Sets the cidade_nascimento of this PerfilUsuario.

        Município em que a pessoa nascida no Brasil nasceu. Formato é o nome lexicograficamente igual a descrição do IBGE ou o código de cidade completo do IBGE  # noqa: E501

        :param cidade_nascimento: The cidade_nascimento of this PerfilUsuario.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cidade_nascimento is not None and len(cidade_nascimento) > 200):
            raise ValueError("Invalid value for `cidade_nascimento`, length must be less than or equal to `200`")  # noqa: E501

        self._cidade_nascimento = cidade_nascimento

    @property
    def pais_nascimento(self):
        """Gets the pais_nascimento of this PerfilUsuario.  # noqa: E501

        País em que a pessoa nasceu. Código ISO 3166-1 alpha-2  # noqa: E501

        :return: The pais_nascimento of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._pais_nascimento

    @pais_nascimento.setter
    def pais_nascimento(self, pais_nascimento):
        """Sets the pais_nascimento of this PerfilUsuario.

        País em que a pessoa nasceu. Código ISO 3166-1 alpha-2  # noqa: E501

        :param pais_nascimento: The pais_nascimento of this PerfilUsuario.  # noqa: E501
        :type: str
        """

        self._pais_nascimento = pais_nascimento

    @property
    def sexo(self):
        """Gets the sexo of this PerfilUsuario.  # noqa: E501

        Sexo do indivíduo  # noqa: E501

        :return: The sexo of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        """Sets the sexo of this PerfilUsuario.

        Sexo do indivíduo  # noqa: E501

        :param sexo: The sexo of this PerfilUsuario.  # noqa: E501
        :type: str
        """
        allowed_values = ["Feminino", "Masculino"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sexo not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sexo` ({0}), must be one of {1}"  # noqa: E501
                .format(sexo, allowed_values)
            )

        self._sexo = sexo

    @property
    def estado_civil(self):
        """Gets the estado_civil of this PerfilUsuario.  # noqa: E501

        Estado civil do usuário  # noqa: E501

        :return: The estado_civil of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil):
        """Sets the estado_civil of this PerfilUsuario.

        Estado civil do usuário  # noqa: E501

        :param estado_civil: The estado_civil of this PerfilUsuario.  # noqa: E501
        :type: str
        """
        allowed_values = ["Casado(a)", "Solteiro(a)", "Divorciado(a)", "União estável", "Separado(a)", "Viúvo(a)"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and estado_civil not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `estado_civil` ({0}), must be one of {1}"  # noqa: E501
                .format(estado_civil, allowed_values)
            )

        self._estado_civil = estado_civil

    @property
    def nome_conjuge(self):
        """Gets the nome_conjuge of this PerfilUsuario.  # noqa: E501

        Nome do conjuge ou companheiro, necessário em casos que o estado civil seja 'Casado(a)' ou 'União estável'  # noqa: E501

        :return: The nome_conjuge of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._nome_conjuge

    @nome_conjuge.setter
    def nome_conjuge(self, nome_conjuge):
        """Sets the nome_conjuge of this PerfilUsuario.

        Nome do conjuge ou companheiro, necessário em casos que o estado civil seja 'Casado(a)' ou 'União estável'  # noqa: E501

        :param nome_conjuge: The nome_conjuge of this PerfilUsuario.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                nome_conjuge is not None and len(nome_conjuge) > 200):
            raise ValueError("Invalid value for `nome_conjuge`, length must be less than or equal to `200`")  # noqa: E501

        self._nome_conjuge = nome_conjuge

    @property
    def nome_mae(self):
        """Gets the nome_mae of this PerfilUsuario.  # noqa: E501

        Nome da mãe do usuário  # noqa: E501

        :return: The nome_mae of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._nome_mae

    @nome_mae.setter
    def nome_mae(self, nome_mae):
        """Sets the nome_mae of this PerfilUsuario.

        Nome da mãe do usuário  # noqa: E501

        :param nome_mae: The nome_mae of this PerfilUsuario.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nome_mae is None:  # noqa: E501
            raise ValueError("Invalid value for `nome_mae`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                nome_mae is not None and len(nome_mae) > 200):
            raise ValueError("Invalid value for `nome_mae`, length must be less than or equal to `200`")  # noqa: E501

        self._nome_mae = nome_mae

    @property
    def nome_pai(self):
        """Gets the nome_pai of this PerfilUsuario.  # noqa: E501

        Nome do pai do usuário. O nome deve ser string vazia ou null caso o pai seja desconhecido.  # noqa: E501

        :return: The nome_pai of this PerfilUsuario.  # noqa: E501
        :rtype: str
        """
        return self._nome_pai

    @nome_pai.setter
    def nome_pai(self, nome_pai):
        """Sets the nome_pai of this PerfilUsuario.

        Nome do pai do usuário. O nome deve ser string vazia ou null caso o pai seja desconhecido.  # noqa: E501

        :param nome_pai: The nome_pai of this PerfilUsuario.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                nome_pai is not None and len(nome_pai) > 200):
            raise ValueError("Invalid value for `nome_pai`, length must be less than or equal to `200`")  # noqa: E501

        self._nome_pai = nome_pai

    @property
    def login(self):
        """Gets the login of this PerfilUsuario.  # noqa: E501


        :return: The login of this PerfilUsuario.  # noqa: E501
        :rtype: LoginObjeto
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this PerfilUsuario.


        :param login: The login of this PerfilUsuario.  # noqa: E501
        :type: LoginObjeto
        """

        self._login = login

    @property
    def documento(self):
        """Gets the documento of this PerfilUsuario.  # noqa: E501


        :return: The documento of this PerfilUsuario.  # noqa: E501
        :rtype: list[Documento]
        """
        return self._documento

    @documento.setter
    def documento(self, documento):
        """Sets the documento of this PerfilUsuario.


        :param documento: The documento of this PerfilUsuario.  # noqa: E501
        :type: list[Documento]
        """
        if self.local_vars_configuration.client_side_validation and documento is None:  # noqa: E501
            raise ValueError("Invalid value for `documento`, must not be `None`")  # noqa: E501

        self._documento = documento

    @property
    def profissao(self):
        """Gets the profissao of this PerfilUsuario.  # noqa: E501


        :return: The profissao of this PerfilUsuario.  # noqa: E501
        :rtype: DadosProfissionais
        """
        return self._profissao

    @profissao.setter
    def profissao(self, profissao):
        """Sets the profissao of this PerfilUsuario.


        :param profissao: The profissao of this PerfilUsuario.  # noqa: E501
        :type: DadosProfissionais
        """

        self._profissao = profissao

    @property
    def endereco(self):
        """Gets the endereco of this PerfilUsuario.  # noqa: E501


        :return: The endereco of this PerfilUsuario.  # noqa: E501
        :rtype: Endereco
        """
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        """Sets the endereco of this PerfilUsuario.


        :param endereco: The endereco of this PerfilUsuario.  # noqa: E501
        :type: Endereco
        """
        if self.local_vars_configuration.client_side_validation and endereco is None:  # noqa: E501
            raise ValueError("Invalid value for `endereco`, must not be `None`")  # noqa: E501

        self._endereco = endereco

    @property
    def patrimonio(self):
        """Gets the patrimonio of this PerfilUsuario.  # noqa: E501


        :return: The patrimonio of this PerfilUsuario.  # noqa: E501
        :rtype: DadosPatrimonial
        """
        return self._patrimonio

    @patrimonio.setter
    def patrimonio(self, patrimonio):
        """Sets the patrimonio of this PerfilUsuario.


        :param patrimonio: The patrimonio of this PerfilUsuario.  # noqa: E501
        :type: DadosPatrimonial
        """

        self._patrimonio = patrimonio

    @property
    def conta_bancaria(self):
        """Gets the conta_bancaria of this PerfilUsuario.  # noqa: E501


        :return: The conta_bancaria of this PerfilUsuario.  # noqa: E501
        :rtype: list[ContaBancaria]
        """
        return self._conta_bancaria

    @conta_bancaria.setter
    def conta_bancaria(self, conta_bancaria):
        """Sets the conta_bancaria of this PerfilUsuario.


        :param conta_bancaria: The conta_bancaria of this PerfilUsuario.  # noqa: E501
        :type: list[ContaBancaria]
        """

        self._conta_bancaria = conta_bancaria

    @property
    def front_end(self):
        """Gets the front_end of this PerfilUsuario.  # noqa: E501


        :return: The front_end of this PerfilUsuario.  # noqa: E501
        :rtype: FrontEndStep
        """
        return self._front_end

    @front_end.setter
    def front_end(self, front_end):
        """Sets the front_end of this PerfilUsuario.


        :param front_end: The front_end of this PerfilUsuario.  # noqa: E501
        :type: FrontEndStep
        """

        self._front_end = front_end

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
        if not isinstance(other, PerfilUsuario):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerfilUsuario):
            return True

        return self.to_dict() != other.to_dict()
