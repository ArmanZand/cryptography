# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

INCLUDES = [
    '#include <openssl/hmac.h>',
]

TYPES = [
    'struct hmac_ctx_st { ...; };',
    'typedef struct hmac_ctx_st HMAC_CTX;',
]

FUNCTIONS = [
    'unsigned char *HMAC(const EVP_MD *evp_md, const void *key,'
        'int key_len, const unsigned char *d, int n,'
        'unsigned char *md, unsigned int *md_len);',
    'void HMAC_CTX_init(HMAC_CTX *ctx);',
    'void HMAC_Init(HMAC_CTX *ctx, const void *key, int key_len, const EVP_MD *md);',
    'void HMAC_Init_ex(HMAC_CTX *ctx, const void *key, int key_len, const EVP_MD *md, ENGINE *impl);',
    'void HMAC_Update(HMAC_CTX *ctx, const unsigned char *data, int len);',
    'void HMAC_Final(HMAC_CTX *ctx, unsigned char *md, unsigned int *len);',
    'void HMAC_CTX_cleanup(HMAC_CTX *ctx);',
    'void HMAC_cleanup(HMAC_CTX *ctx);',
]
