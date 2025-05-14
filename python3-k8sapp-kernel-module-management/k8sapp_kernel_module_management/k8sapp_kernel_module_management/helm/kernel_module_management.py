#
# Copyright (c) 2025 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

from k8sapp_kernel_module_management.common import constants as app_constants

from sysinv.helm import base
from sysinv.common import exception

class KernelModuleManagementHelm(base.FluxCDBaseHelm):
    """Class to encapsulate helm operations for the app chart"""

    SUPPORTED_NAMESPACES = base.BaseHelm.SUPPORTED_NAMESPACES + \
        [app_constants.HELM_NS_KERNEL_MODULE_MANAGEMENT]

    SUPPORTED_APP_NAMESPACES = {app_constants.HELM_APP_KERNEL_MODULE_MANAGEMENT : SUPPORTED_NAMESPACES,
    }

    CHART = app_constants.HELM_CHART_KERNEL_MODULE_MANAGEMENT
    HELM_RELEASE = app_constants.FLUXCD_HELMRELEASE_KERNEL_MODULE_MANAGEMENT

    def get_namespaces(self):
        return self.SUPPORTED_NAMESPACES

    def get_overrides(self, namespace=None):

        overrides = {
            app_constants.HELM_NS_KERNEL_MODULE_MANAGEMENT: {}
        }

        if namespace in self.SUPPORTED_NAMESPACES:
            return overrides[namespace]
        elif namespace:
            raise exception.InvalidHelmNamespace(chart=self.CHART,
                                                 namespace=namespace)
        else:
            return overrides
