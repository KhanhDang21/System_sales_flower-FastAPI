from schemas.base_response import BaseResponse

ERROR_CODES = {
    1001: 'Login failed!',
    1002: 'Credentials are not correct!',
    1003: 'Register failed!',
    2001: 'Get flowers failed!',
    2002: 'Create flower failed!',
    2003: 'Update flower failed!',
    2004: 'Delete flower failed!',
    3001: 'Get bills failed',
    3002: 'Create bills failed',
    3003: 'Update bills failed',
    3004: 'Delete bills failed'
}


def raise_error(error_code: int) -> BaseResponse:
    return BaseResponse(
        message=ERROR_CODES.get(error_code),
        status='error',
    )
