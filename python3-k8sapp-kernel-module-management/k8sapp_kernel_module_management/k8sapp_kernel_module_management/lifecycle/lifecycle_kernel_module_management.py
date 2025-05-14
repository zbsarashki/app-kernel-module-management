""" System inventory App lifecycle operator."""

from oslo_log import log as logging
from sysinv.common import constants
from sysinv.helm import lifecycle_base as base
from sysinv.helm import lifecycle_utils as lifecycle_utils

LOG = logging.getLogger(__name__)

class KernelModuleManagementAppLifecycleOperator(base.AppLifecycleOperator):

    def app_lifecycle_actions(self, context, conductor_obj, app_op, app, hook_info):
        """ Perform lifecycle actions for an operation

        :param context: request context
        :param conductor_obj: conductor object
        :param app_op: AppOperator object
        :param app: AppOperator.Application object
        :param hook_info: LifecycleHookInfo object

        """
        pass
