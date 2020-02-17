# cadastro_orama.UsersApi

All URIs are relative to *https://cadastro.orama.com.br/api/contas/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_autenticacao_post**](UsersApi.md#account_autenticacao_post) | **POST** /autenticacao/ | Autentica um usuário que ainda não é cliente.
[**account_documento_confirmacao_get**](UsersApi.md#account_documento_confirmacao_get) | **GET** /perfil/{cpf}/documento/confirmacao/ | Consulta o status de confirmação do documento que foi submetido
[**account_documento_put**](UsersApi.md#account_documento_put) | **PUT** /perfil/{cpf}/documento/ | Anexa ou atualiza documento para conferencia de autenticidade do perfil.
[**account_identificacao_post**](UsersApi.md#account_identificacao_post) | **POST** /identificacao/ | Cria um login para usuário.
[**account_perfil_aprovacao_get**](UsersApi.md#account_perfil_aprovacao_get) | **GET** /perfil/{cpf}/aprovacao/ | Retorna o estado de aprovação de um perfil
[**account_perfil_assinatura_eletronica_get**](UsersApi.md#account_perfil_assinatura_eletronica_get) | **GET** /perfil/{cpf}/assinatura-eletronica/ | Verifica se a assinatura eletronica já foi definida.
[**account_perfil_assinatura_eletronica_post**](UsersApi.md#account_perfil_assinatura_eletronica_post) | **POST** /perfil/{cpf}/assinatura-eletronica/ | Realiza o cadastro da assinatura eletrônica do perfil.
[**account_perfil_celular_autenticacao_confirmacao_get**](UsersApi.md#account_perfil_celular_autenticacao_confirmacao_get) | **GET** /perfil/{cpf}/celular/autenticacao/confirmacao/ | Estado atual de confirmação do celular
[**account_perfil_celular_autenticacao_post**](UsersApi.md#account_perfil_celular_autenticacao_post) | **POST** /perfil/{cpf}/celular/autenticacao/ | Gera um código para iniciar o processo de validação do número do celular
[**account_perfil_celular_confirmacao_post**](UsersApi.md#account_perfil_celular_confirmacao_post) | **POST** /perfil/{cpf}/celular/autenticacao/confirmacao/ | Confirma o numero de celular, concluindo a validação
[**account_perfil_email_autenticacao_confirmacao_get**](UsersApi.md#account_perfil_email_autenticacao_confirmacao_get) | **GET** /perfil/{cpf}/email/autenticacao/confirmacao/ | Estado atual de confirmação do email
[**account_perfil_email_autenticacao_post**](UsersApi.md#account_perfil_email_autenticacao_post) | **POST** /perfil/{cpf}/email/autenticacao/ | Gera um código para iniciar o processo de validação do email
[**account_perfil_email_confirmacao_post**](UsersApi.md#account_perfil_email_confirmacao_post) | **POST** /perfil/{cpf}/email/autenticacao/confirmacao/ | Confirma o email, concluindo a validação
[**account_perfil_get**](UsersApi.md#account_perfil_get) | **GET** /perfil/{cpf}/ | Retorna o perfil de um usuário que ainda não foi transformado em cliente.
[**account_perfil_post**](UsersApi.md#account_perfil_post) | **POST** /perfil/{cpf}/ | Submete o perfil de usuário associado a um login para ser criado como cliente.
[**account_perfil_put**](UsersApi.md#account_perfil_put) | **PUT** /perfil/{cpf}/ | Atualiza perfil para criação de conta.
[**account_perfil_submetido_get**](UsersApi.md#account_perfil_submetido_get) | **GET** /perfil/{cpf}/submetido/ | Retorna o estado de submissão de um perfil
[**account_perfil_termos_confirmacao_get**](UsersApi.md#account_perfil_termos_confirmacao_get) | **GET** /perfil/{cpf}/termos/confirmacao/ | Estado atual de confirmação do aceite de termos
[**account_perfil_termos_confirmacao_post**](UsersApi.md#account_perfil_termos_confirmacao_post) | **POST** /perfil/{cpf}/termos/confirmacao/ | Confirma o aceite de termos
[**account_perfil_termos_get**](UsersApi.md#account_perfil_termos_get) | **GET** /perfil/{cpf}/termos/ | Consulta os termos requeridos para o perfil


# **account_autenticacao_post**
> AutenticacaoObjeto account_autenticacao_post(usuario_senha_objeto)

Autentica um usuário que ainda não é cliente.

Autentica um usuário que ainda não é cliente, caso o usuário não existe, ou a combinação de usuário e senha ou ainda o usuário já seja cliente retorna um erro.

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    usuario_senha_objeto = cadastro_orama.UsuarioSenhaObjeto() # UsuarioSenhaObjeto | Dados para autenticação do usuário

    try:
        # Autentica um usuário que ainda não é cliente.
        api_response = api_instance.account_autenticacao_post(usuario_senha_objeto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_autenticacao_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usuario_senha_objeto** | [**UsuarioSenhaObjeto**](UsuarioSenhaObjeto.md)| Dados para autenticação do usuário | 

### Return type

[**AutenticacaoObjeto**](AutenticacaoObjeto.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Autenticado |  -  |
**401** | Autenticação inválida |  -  |
**403** | Não Autorizado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_documento_confirmacao_get**
> account_documento_confirmacao_get(cpf, tipo_documento)

Consulta o status de confirmação do documento que foi submetido

Consulta o status de confirmação do documento que foi submetido

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil
tipo_documento = 'Passaporte' # str | Tipo do documento

    try:
        # Consulta o status de confirmação do documento que foi submetido
        api_instance.account_documento_confirmacao_get(cpf, tipo_documento)
    except ApiException as e:
        print("Exception when calling UsersApi->account_documento_confirmacao_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 
 **tipo_documento** | **str**| Tipo do documento | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Documento enviado com sucesso |  -  |
**202** | Upload em progresso |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_documento_put**
> account_documento_put(cpf, tipo_documento, filename)

Anexa ou atualiza documento para conferencia de autenticidade do perfil.

Anexa ou atualiza documento que será usado no processo conferencia de autenticidade do perfil. É recomendado fazer o upload de documentos para comprovação de identidade. Caso o perfil tiver conta bancária conjunta ou a conta seja do banco Itaú é recomendado o upload do documento 'Comprovante Bancário'.

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil
tipo_documento = 'Passaporte' # str | Tipo do documento
filename = '/path/to/file' # file | Arquivo binário que será enviado. O formato deve ser PDF, PNG ou JPG

    try:
        # Anexa ou atualiza documento para conferencia de autenticidade do perfil.
        api_instance.account_documento_put(cpf, tipo_documento, filename)
    except ApiException as e:
        print("Exception when calling UsersApi->account_documento_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 
 **tipo_documento** | **str**| Tipo do documento | 
 **filename** | **file**| Arquivo binário que será enviado. O formato deve ser PDF, PNG ou JPG | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Arquivo aceito |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_identificacao_post**
> LoginCriado account_identificacao_post(login_senha_objeto)

Cria um login para usuário.

Cria um novo login que será usado para acesso ao sistema.

### Example

```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    login_senha_objeto = cadastro_orama.LoginSenhaObjeto() # LoginSenhaObjeto | Dados para criação do login

    try:
        # Cria um login para usuário.
        api_response = api_instance.account_identificacao_post(login_senha_objeto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_identificacao_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_senha_objeto** | [**LoginSenhaObjeto**](LoginSenhaObjeto.md)| Dados para criação do login | 

### Return type

[**LoginCriado**](LoginCriado.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Login criado |  -  |
**400** | Dados inválidos ou incompletos |  -  |
**405** | Metodo não permitido |  -  |
**409** | CPF, celular ou e-mail duplicados |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_aprovacao_get**
> Aprovacao account_perfil_aprovacao_get(cpf)

Retorna o estado de aprovação de um perfil

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Retorna o estado de aprovação de um perfil
        api_response = api_instance.account_perfil_aprovacao_get(cpf)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_aprovacao_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

[**Aprovacao**](Aprovacao.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retorna o estado atual de aprovação |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_assinatura_eletronica_get**
> account_perfil_assinatura_eletronica_get(cpf)

Verifica se a assinatura eletronica já foi definida.

Verifica se a assinatura eletronica já foi definida.

### Example

* Api Key Authentication (Api-Key):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure API key authorization: Api-Key
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Verifica se a assinatura eletronica já foi definida.
        api_instance.account_perfil_assinatura_eletronica_get(cpf)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_assinatura_eletronica_get: %s\n" % e)
```

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure API key authorization: Api-Key
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Verifica se a assinatura eletronica já foi definida.
        api_instance.account_perfil_assinatura_eletronica_get(cpf)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_assinatura_eletronica_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

void (empty response body)

### Authorization

[Api-Key](../README.md#Api-Key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | assinatura eletronica já esta definida |  -  |
**404** | assinatura eletronica não encontrada |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_assinatura_eletronica_post**
> account_perfil_assinatura_eletronica_post(cpf, assinatura_eletronica)

Realiza o cadastro da assinatura eletrônica do perfil.

Cadastra a assinatura eletrônica do perfil, realiza validação da assinatura eletronica.  A assinatura deve respeitar as seguintes condições: - Conter de 6 a 15 dígitos - Conter apenas letras e números - Não deve conter 6 ou mais dígitos sequênciais, ex.: 'abcdef', '123456' - Se a assinatura contém entre 6 e 7 dígitos não deve repetir 3 dígitos seguidos, ex.: '111', 'aaa' - Se a assinatura contém entre 8 e 12 dígitos não deve repetir 4 dígitos seguidos, ex.: '1111', 'aaaa' - Se a assinatura contém entre 13 e 14 dígitos não deve repetir 5 dígitos seguidos, ex.: '11111', 'aaaaa' - Se a assinatura contém 15 dígitos não deve repetir 6 dígitos seguidos, ex.: '111111', 'aaaaaa' - A assinatura não deve conter nenhuma das palavras a seguir:      'select', 'update', 'insert', 'delete', 'drop', 'truncate', 'waitfor', 'delay', 'where', 'from', 'having', 'script', 'applet', 'sha1'

### Example

* Api Key Authentication (Api-Key):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure API key authorization: Api-Key
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil
assinatura_eletronica = cadastro_orama.AssinaturaEletronica() # AssinaturaEletronica | Dados para criação da assinatura eletrônica

    try:
        # Realiza o cadastro da assinatura eletrônica do perfil.
        api_instance.account_perfil_assinatura_eletronica_post(cpf, assinatura_eletronica)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_assinatura_eletronica_post: %s\n" % e)
```

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure API key authorization: Api-Key
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil
assinatura_eletronica = cadastro_orama.AssinaturaEletronica() # AssinaturaEletronica | Dados para criação da assinatura eletrônica

    try:
        # Realiza o cadastro da assinatura eletrônica do perfil.
        api_instance.account_perfil_assinatura_eletronica_post(cpf, assinatura_eletronica)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_assinatura_eletronica_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 
 **assinatura_eletronica** | [**AssinaturaEletronica**](AssinaturaEletronica.md)| Dados para criação da assinatura eletrônica | 

### Return type

void (empty response body)

### Authorization

[Api-Key](../README.md#Api-Key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | assinatura eletrônica criada. |  -  |
**400** | Dados inválidos ou incompletos |  -  |
**409** | perfil não pode mais ser modificado por esta chamada de API |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_celular_autenticacao_confirmacao_get**
> Confirmado account_perfil_celular_autenticacao_confirmacao_get(cpf)

Estado atual de confirmação do celular

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Estado atual de confirmação do celular
        api_response = api_instance.account_perfil_celular_autenticacao_confirmacao_get(cpf)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_celular_autenticacao_confirmacao_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

[**Confirmado**](Confirmado.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmado |  -  |
**202** | Envio do SMS esta sendo processado |  -  |
**400** | Erro encontrado durante a validação através de SMS |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_celular_autenticacao_post**
> account_perfil_celular_autenticacao_post(cpf)

Gera um código para iniciar o processo de validação do número do celular

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Gera um código para iniciar o processo de validação do número do celular
        api_instance.account_perfil_celular_autenticacao_post(cpf)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_celular_autenticacao_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | O processo de validação para gerar o código foi iniciado |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_celular_confirmacao_post**
> Confirmado account_perfil_celular_confirmacao_post(cpf, codigo)

Confirma o numero de celular, concluindo a validação

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil
codigo = '1341' # str | Código de validação para confirmar o número de celular

    try:
        # Confirma o numero de celular, concluindo a validação
        api_response = api_instance.account_perfil_celular_confirmacao_post(cpf, codigo)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_celular_confirmacao_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 
 **codigo** | **str**| Código de validação para confirmar o número de celular | 

### Return type

[**Confirmado**](Confirmado.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Confirmado |  -  |
**202** | Envio do SMS esta sendo processado |  -  |
**400** | Erro encontrado durante a validação através de SMS |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**409** | Este número de celular já foi validado |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_email_autenticacao_confirmacao_get**
> Confirmado account_perfil_email_autenticacao_confirmacao_get(cpf)

Estado atual de confirmação do email

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Estado atual de confirmação do email
        api_response = api_instance.account_perfil_email_autenticacao_confirmacao_get(cpf)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_email_autenticacao_confirmacao_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

[**Confirmado**](Confirmado.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmado |  -  |
**202** | Envio do e-mail esta sendo processado |  -  |
**400** | Erro encontrado durante a validação através de e-mail |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_email_autenticacao_post**
> account_perfil_email_autenticacao_post(cpf)

Gera um código para iniciar o processo de validação do email

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Gera um código para iniciar o processo de validação do email
        api_instance.account_perfil_email_autenticacao_post(cpf)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_email_autenticacao_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | O processo de validação para gerar o código foi iniciado |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_email_confirmacao_post**
> Confirmado account_perfil_email_confirmacao_post(cpf, codigo)

Confirma o email, concluindo a validação

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil
codigo = '1341' # str | Código de validação para confirmar o email

    try:
        # Confirma o email, concluindo a validação
        api_response = api_instance.account_perfil_email_confirmacao_post(cpf, codigo)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_email_confirmacao_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 
 **codigo** | **str**| Código de validação para confirmar o email | 

### Return type

[**Confirmado**](Confirmado.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Confirmado |  -  |
**202** | Envio do e-mail esta sendo processado |  -  |
**400** | Erro encontrado durante a validação através de e-mail |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**409** | Este e-mail já foi validado |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_get**
> PerfilUsuario account_perfil_get(cpf, campos=campos)

Retorna o perfil de um usuário que ainda não foi transformado em cliente.

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil
campos = 'login,profissao,usPerson' # str | Lista de campos para ser inclusivamente filtrados (optional)

    try:
        # Retorna o perfil de um usuário que ainda não foi transformado em cliente.
        api_response = api_instance.account_perfil_get(cpf, campos=campos)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 
 **campos** | **str**| Lista de campos para ser inclusivamente filtrados | [optional] 

### Return type

[**PerfilUsuario**](PerfilUsuario.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ok |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_post**
> account_perfil_post(cpf)

Submete o perfil de usuário associado a um login para ser criado como cliente.

Submete o perfil de usuário associado a um login para ser criado como cliente. A assinatura eletrônica é obrigatória para a submissão do usuário, ver endpoint /perfil/{cpf}/assinatura-eletronica/. É necessário validar ambos o número do celular e o e-mail para que a submissão seja aceita, veja os endpoints /perfil/{cpf}/celular/autenticacao/ e /perfil/{cpf}/email/autenticacao/. Após submissão deste POST, o perfil não poderá mais ser alterado. Para alterar ou inserir informações no perfil antes de submeter o perfil o método PUT deve ser utilizado.

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Submete o perfil de usuário associado a um login para ser criado como cliente.
        api_instance.account_perfil_post(cpf)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | O perfil foi submetido para ser criado. |  -  |
**400** | Dados inválidos ou incompletos |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**409** | Este perfil já foi submetido ou outros conflitos de submissões mandatórios |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_put**
> account_perfil_put(cpf, perfil_usuario)

Atualiza perfil para criação de conta.

Atualiza um perfil de usuário associado a um login para o processo de criação de um usuário. Cada chamada modifica o perfil. Quando o perfil estiver pronto para ser submetido para criação de conta, basta enviar um POST.

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil
perfil_usuario = cadastro_orama.PerfilUsuario() # PerfilUsuario | Dados para criação ou atualização do perfil

    try:
        # Atualiza perfil para criação de conta.
        api_instance.account_perfil_put(cpf, perfil_usuario)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 
 **perfil_usuario** | [**PerfilUsuario**](PerfilUsuario.md)| Dados para criação ou atualização do perfil | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | perfil atualizado |  -  |
**400** | Dados inválidos ou incompletos |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**405** | Metodo não permitido |  -  |
**409** | perfil não pode mais ser modificado por esta chamada de API |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_submetido_get**
> Submetido account_perfil_submetido_get(cpf)

Retorna o estado de submissão de um perfil

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Retorna o estado de submissão de um perfil
        api_response = api_instance.account_perfil_submetido_get(cpf)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_submetido_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

[**Submetido**](Submetido.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retorna o estado atual de submissão |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_termos_confirmacao_get**
> Confirmado account_perfil_termos_confirmacao_get(cpf)

Estado atual de confirmação do aceite de termos

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Estado atual de confirmação do aceite de termos
        api_response = api_instance.account_perfil_termos_confirmacao_get(cpf)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_termos_confirmacao_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

[**Confirmado**](Confirmado.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmado |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_termos_confirmacao_post**
> Confirmado account_perfil_termos_confirmacao_post(cpf)

Confirma o aceite de termos

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Confirma o aceite de termos
        api_response = api_instance.account_perfil_termos_confirmacao_post(cpf)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_termos_confirmacao_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

[**Confirmado**](Confirmado.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Confirmado |  -  |
**400** | Erro encontrado durante o aceite de termos |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**409** | Este perfil já aceitou os termos |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_perfil_termos_get**
> list[Termos] account_perfil_termos_get(cpf)

Consulta os termos requeridos para o perfil

Consulta os termos exigidos para o perfil

### Example

* Bearer (JWT) Authentication (JWT):
```python
from __future__ import print_function
import time
import cadastro_orama
from cadastro_orama.rest import ApiException
from pprint import pprint
configuration = cadastro_orama.Configuration()
# Configure Bearer authorization (JWT): JWT
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://cadastro.orama.com.br/api/contas/v2.0
configuration.host = "https://cadastro.orama.com.br/api/contas/v2.0"

# Enter a context with an instance of the API client
with cadastro_orama.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cadastro_orama.UsersApi(api_client)
    cpf = 'cpf_example' # str | CPF do perfil

    try:
        # Consulta os termos requeridos para o perfil
        api_response = api_instance.account_perfil_termos_get(cpf)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->account_perfil_termos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpf** | **str**| CPF do perfil | 

### Return type

[**list[Termos]**](Termos.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Termos e Declarações requeridos |  -  |
**401** | Token inválido |  -  |
**403** | Não Autorizado |  -  |
**404** | CPF não encontrado |  -  |
**405** | Metodo não permitido |  -  |
**429** | Limite de requisições por segundo foi alcançado. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

