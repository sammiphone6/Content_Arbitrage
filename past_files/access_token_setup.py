from ig_defines import makeApiCall
"""
https://api.instagram.com/oauth/authorize
  ?client_id={app-id},
  &redirect_uri={redirect-uri},
  &response_type=code,
  &scope={scope}
"""

###### THIS IS NOT COMPLETE OR WORKING ######

url = 'https://api.instagram.com/oauth/authorize'

endpointParams = dict()

## Edit these
endpointParams['client_id'] = '' ##This is the instagram basic display id
endpointParams['redirect_uri'] = 'https://www.youtube.com'
endpointParams['response_type'] = 'code'
endpointParams['client_id'] = 'user_profile,user_media'

## Edit these


response = makeApiCall(url, endpointParams, 'GET')


print(response)