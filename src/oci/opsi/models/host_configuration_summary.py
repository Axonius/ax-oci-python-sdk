# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostConfigurationSummary(object):
    """
    Summary of a host configuration for a resource.
    """

    #: A constant which can be used with the entity_source property of a HostConfigurationSummary.
    #: This constant has a value of "MACS_MANAGED_EXTERNAL_HOST"
    ENTITY_SOURCE_MACS_MANAGED_EXTERNAL_HOST = "MACS_MANAGED_EXTERNAL_HOST"

    #: A constant which can be used with the entity_source property of a HostConfigurationSummary.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_HOST"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_HOST = "EM_MANAGED_EXTERNAL_HOST"

    #: A constant which can be used with the entity_source property of a HostConfigurationSummary.
    #: This constant has a value of "PE_COMANAGED_HOST"
    ENTITY_SOURCE_PE_COMANAGED_HOST = "PE_COMANAGED_HOST"

    #: A constant which can be used with the platform_type property of a HostConfigurationSummary.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a HostConfigurationSummary.
    #: This constant has a value of "SOLARIS"
    PLATFORM_TYPE_SOLARIS = "SOLARIS"

    #: A constant which can be used with the platform_type property of a HostConfigurationSummary.
    #: This constant has a value of "SUNOS"
    PLATFORM_TYPE_SUNOS = "SUNOS"

    #: A constant which can be used with the platform_type property of a HostConfigurationSummary.
    #: This constant has a value of "ZLINUX"
    PLATFORM_TYPE_ZLINUX = "ZLINUX"

    def __init__(self, **kwargs):
        """
        Initializes a new HostConfigurationSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.MacsManagedExternalHostConfigurationSummary`
        * :class:`~oci.opsi.models.PeComanagedHostConfigurationSummary`
        * :class:`~oci.opsi.models.EmManagedExternalHostConfigurationSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_insight_id:
            The value to assign to the host_insight_id property of this HostConfigurationSummary.
        :type host_insight_id: str

        :param entity_source:
            The value to assign to the entity_source property of this HostConfigurationSummary.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST", "PE_COMANAGED_HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this HostConfigurationSummary.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this HostConfigurationSummary.
        :type host_name: str

        :param platform_type:
            The value to assign to the platform_type property of this HostConfigurationSummary.
            Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        :param platform_version:
            The value to assign to the platform_version property of this HostConfigurationSummary.
        :type platform_version: str

        :param platform_vendor:
            The value to assign to the platform_vendor property of this HostConfigurationSummary.
        :type platform_vendor: str

        :param total_cpus:
            The value to assign to the total_cpus property of this HostConfigurationSummary.
        :type total_cpus: int

        :param total_memory_in_gbs:
            The value to assign to the total_memory_in_gbs property of this HostConfigurationSummary.
        :type total_memory_in_gbs: float

        :param cpu_architecture:
            The value to assign to the cpu_architecture property of this HostConfigurationSummary.
        :type cpu_architecture: str

        :param cpu_cache_in_mbs:
            The value to assign to the cpu_cache_in_mbs property of this HostConfigurationSummary.
        :type cpu_cache_in_mbs: float

        :param cpu_vendor:
            The value to assign to the cpu_vendor property of this HostConfigurationSummary.
        :type cpu_vendor: str

        :param cpu_frequency_in_mhz:
            The value to assign to the cpu_frequency_in_mhz property of this HostConfigurationSummary.
        :type cpu_frequency_in_mhz: float

        :param cpu_implementation:
            The value to assign to the cpu_implementation property of this HostConfigurationSummary.
        :type cpu_implementation: str

        :param cores_per_socket:
            The value to assign to the cores_per_socket property of this HostConfigurationSummary.
        :type cores_per_socket: int

        :param total_sockets:
            The value to assign to the total_sockets property of this HostConfigurationSummary.
        :type total_sockets: int

        :param threads_per_socket:
            The value to assign to the threads_per_socket property of this HostConfigurationSummary.
        :type threads_per_socket: int

        :param is_hyper_threading_enabled:
            The value to assign to the is_hyper_threading_enabled property of this HostConfigurationSummary.
        :type is_hyper_threading_enabled: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this HostConfigurationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this HostConfigurationSummary.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'host_insight_id': 'str',
            'entity_source': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'platform_type': 'str',
            'platform_version': 'str',
            'platform_vendor': 'str',
            'total_cpus': 'int',
            'total_memory_in_gbs': 'float',
            'cpu_architecture': 'str',
            'cpu_cache_in_mbs': 'float',
            'cpu_vendor': 'str',
            'cpu_frequency_in_mhz': 'float',
            'cpu_implementation': 'str',
            'cores_per_socket': 'int',
            'total_sockets': 'int',
            'threads_per_socket': 'int',
            'is_hyper_threading_enabled': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'host_insight_id': 'hostInsightId',
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'platform_type': 'platformType',
            'platform_version': 'platformVersion',
            'platform_vendor': 'platformVendor',
            'total_cpus': 'totalCpus',
            'total_memory_in_gbs': 'totalMemoryInGBs',
            'cpu_architecture': 'cpuArchitecture',
            'cpu_cache_in_mbs': 'cpuCacheInMBs',
            'cpu_vendor': 'cpuVendor',
            'cpu_frequency_in_mhz': 'cpuFrequencyInMhz',
            'cpu_implementation': 'cpuImplementation',
            'cores_per_socket': 'coresPerSocket',
            'total_sockets': 'totalSockets',
            'threads_per_socket': 'threadsPerSocket',
            'is_hyper_threading_enabled': 'isHyperThreadingEnabled',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._host_insight_id = None
        self._entity_source = None
        self._compartment_id = None
        self._host_name = None
        self._platform_type = None
        self._platform_version = None
        self._platform_vendor = None
        self._total_cpus = None
        self._total_memory_in_gbs = None
        self._cpu_architecture = None
        self._cpu_cache_in_mbs = None
        self._cpu_vendor = None
        self._cpu_frequency_in_mhz = None
        self._cpu_implementation = None
        self._cores_per_socket = None
        self._total_sockets = None
        self._threads_per_socket = None
        self._is_hyper_threading_enabled = None
        self._defined_tags = None
        self._freeform_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'MACS_MANAGED_EXTERNAL_HOST':
            return 'MacsManagedExternalHostConfigurationSummary'

        if type == 'PE_COMANAGED_HOST':
            return 'PeComanagedHostConfigurationSummary'

        if type == 'EM_MANAGED_EXTERNAL_HOST':
            return 'EmManagedExternalHostConfigurationSummary'
        else:
            return 'HostConfigurationSummary'

    @property
    def host_insight_id(self):
        """
        **[Required]** Gets the host_insight_id of this HostConfigurationSummary.
        The `OCID`__ of the host insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The host_insight_id of this HostConfigurationSummary.
        :rtype: str
        """
        return self._host_insight_id

    @host_insight_id.setter
    def host_insight_id(self, host_insight_id):
        """
        Sets the host_insight_id of this HostConfigurationSummary.
        The `OCID`__ of the host insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param host_insight_id: The host_insight_id of this HostConfigurationSummary.
        :type: str
        """
        self._host_insight_id = host_insight_id

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this HostConfigurationSummary.
        Source of the host entity.

        Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST", "PE_COMANAGED_HOST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_source of this HostConfigurationSummary.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this HostConfigurationSummary.
        Source of the host entity.


        :param entity_source: The entity_source of this HostConfigurationSummary.
        :type: str
        """
        allowed_values = ["MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST", "PE_COMANAGED_HOST"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            entity_source = 'UNKNOWN_ENUM_VALUE'
        self._entity_source = entity_source

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this HostConfigurationSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this HostConfigurationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this HostConfigurationSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this HostConfigurationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this HostConfigurationSummary.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :return: The host_name of this HostConfigurationSummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this HostConfigurationSummary.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :param host_name: The host_name of this HostConfigurationSummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def platform_type(self):
        """
        **[Required]** Gets the platform_type of this HostConfigurationSummary.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].

        Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this HostConfigurationSummary.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this HostConfigurationSummary.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].


        :param platform_type: The platform_type of this HostConfigurationSummary.
        :type: str
        """
        allowed_values = ["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    @property
    def platform_version(self):
        """
        **[Required]** Gets the platform_version of this HostConfigurationSummary.
        Platform version.


        :return: The platform_version of this HostConfigurationSummary.
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """
        Sets the platform_version of this HostConfigurationSummary.
        Platform version.


        :param platform_version: The platform_version of this HostConfigurationSummary.
        :type: str
        """
        self._platform_version = platform_version

    @property
    def platform_vendor(self):
        """
        **[Required]** Gets the platform_vendor of this HostConfigurationSummary.
        Platform vendor.


        :return: The platform_vendor of this HostConfigurationSummary.
        :rtype: str
        """
        return self._platform_vendor

    @platform_vendor.setter
    def platform_vendor(self, platform_vendor):
        """
        Sets the platform_vendor of this HostConfigurationSummary.
        Platform vendor.


        :param platform_vendor: The platform_vendor of this HostConfigurationSummary.
        :type: str
        """
        self._platform_vendor = platform_vendor

    @property
    def total_cpus(self):
        """
        **[Required]** Gets the total_cpus of this HostConfigurationSummary.
        Total CPU on this host.


        :return: The total_cpus of this HostConfigurationSummary.
        :rtype: int
        """
        return self._total_cpus

    @total_cpus.setter
    def total_cpus(self, total_cpus):
        """
        Sets the total_cpus of this HostConfigurationSummary.
        Total CPU on this host.


        :param total_cpus: The total_cpus of this HostConfigurationSummary.
        :type: int
        """
        self._total_cpus = total_cpus

    @property
    def total_memory_in_gbs(self):
        """
        **[Required]** Gets the total_memory_in_gbs of this HostConfigurationSummary.
        Total amount of usable physical memory in gibabytes


        :return: The total_memory_in_gbs of this HostConfigurationSummary.
        :rtype: float
        """
        return self._total_memory_in_gbs

    @total_memory_in_gbs.setter
    def total_memory_in_gbs(self, total_memory_in_gbs):
        """
        Sets the total_memory_in_gbs of this HostConfigurationSummary.
        Total amount of usable physical memory in gibabytes


        :param total_memory_in_gbs: The total_memory_in_gbs of this HostConfigurationSummary.
        :type: float
        """
        self._total_memory_in_gbs = total_memory_in_gbs

    @property
    def cpu_architecture(self):
        """
        **[Required]** Gets the cpu_architecture of this HostConfigurationSummary.
        CPU architechure


        :return: The cpu_architecture of this HostConfigurationSummary.
        :rtype: str
        """
        return self._cpu_architecture

    @cpu_architecture.setter
    def cpu_architecture(self, cpu_architecture):
        """
        Sets the cpu_architecture of this HostConfigurationSummary.
        CPU architechure


        :param cpu_architecture: The cpu_architecture of this HostConfigurationSummary.
        :type: str
        """
        self._cpu_architecture = cpu_architecture

    @property
    def cpu_cache_in_mbs(self):
        """
        **[Required]** Gets the cpu_cache_in_mbs of this HostConfigurationSummary.
        Size of cache memory in megabytes.


        :return: The cpu_cache_in_mbs of this HostConfigurationSummary.
        :rtype: float
        """
        return self._cpu_cache_in_mbs

    @cpu_cache_in_mbs.setter
    def cpu_cache_in_mbs(self, cpu_cache_in_mbs):
        """
        Sets the cpu_cache_in_mbs of this HostConfigurationSummary.
        Size of cache memory in megabytes.


        :param cpu_cache_in_mbs: The cpu_cache_in_mbs of this HostConfigurationSummary.
        :type: float
        """
        self._cpu_cache_in_mbs = cpu_cache_in_mbs

    @property
    def cpu_vendor(self):
        """
        **[Required]** Gets the cpu_vendor of this HostConfigurationSummary.
        Name of the CPU vendor.


        :return: The cpu_vendor of this HostConfigurationSummary.
        :rtype: str
        """
        return self._cpu_vendor

    @cpu_vendor.setter
    def cpu_vendor(self, cpu_vendor):
        """
        Sets the cpu_vendor of this HostConfigurationSummary.
        Name of the CPU vendor.


        :param cpu_vendor: The cpu_vendor of this HostConfigurationSummary.
        :type: str
        """
        self._cpu_vendor = cpu_vendor

    @property
    def cpu_frequency_in_mhz(self):
        """
        **[Required]** Gets the cpu_frequency_in_mhz of this HostConfigurationSummary.
        Clock frequency of the processor in megahertz.


        :return: The cpu_frequency_in_mhz of this HostConfigurationSummary.
        :rtype: float
        """
        return self._cpu_frequency_in_mhz

    @cpu_frequency_in_mhz.setter
    def cpu_frequency_in_mhz(self, cpu_frequency_in_mhz):
        """
        Sets the cpu_frequency_in_mhz of this HostConfigurationSummary.
        Clock frequency of the processor in megahertz.


        :param cpu_frequency_in_mhz: The cpu_frequency_in_mhz of this HostConfigurationSummary.
        :type: float
        """
        self._cpu_frequency_in_mhz = cpu_frequency_in_mhz

    @property
    def cpu_implementation(self):
        """
        **[Required]** Gets the cpu_implementation of this HostConfigurationSummary.
        Model name of processor.


        :return: The cpu_implementation of this HostConfigurationSummary.
        :rtype: str
        """
        return self._cpu_implementation

    @cpu_implementation.setter
    def cpu_implementation(self, cpu_implementation):
        """
        Sets the cpu_implementation of this HostConfigurationSummary.
        Model name of processor.


        :param cpu_implementation: The cpu_implementation of this HostConfigurationSummary.
        :type: str
        """
        self._cpu_implementation = cpu_implementation

    @property
    def cores_per_socket(self):
        """
        **[Required]** Gets the cores_per_socket of this HostConfigurationSummary.
        Number of cores per socket.


        :return: The cores_per_socket of this HostConfigurationSummary.
        :rtype: int
        """
        return self._cores_per_socket

    @cores_per_socket.setter
    def cores_per_socket(self, cores_per_socket):
        """
        Sets the cores_per_socket of this HostConfigurationSummary.
        Number of cores per socket.


        :param cores_per_socket: The cores_per_socket of this HostConfigurationSummary.
        :type: int
        """
        self._cores_per_socket = cores_per_socket

    @property
    def total_sockets(self):
        """
        **[Required]** Gets the total_sockets of this HostConfigurationSummary.
        Number of total sockets.


        :return: The total_sockets of this HostConfigurationSummary.
        :rtype: int
        """
        return self._total_sockets

    @total_sockets.setter
    def total_sockets(self, total_sockets):
        """
        Sets the total_sockets of this HostConfigurationSummary.
        Number of total sockets.


        :param total_sockets: The total_sockets of this HostConfigurationSummary.
        :type: int
        """
        self._total_sockets = total_sockets

    @property
    def threads_per_socket(self):
        """
        **[Required]** Gets the threads_per_socket of this HostConfigurationSummary.
        Number of threads per socket.


        :return: The threads_per_socket of this HostConfigurationSummary.
        :rtype: int
        """
        return self._threads_per_socket

    @threads_per_socket.setter
    def threads_per_socket(self, threads_per_socket):
        """
        Sets the threads_per_socket of this HostConfigurationSummary.
        Number of threads per socket.


        :param threads_per_socket: The threads_per_socket of this HostConfigurationSummary.
        :type: int
        """
        self._threads_per_socket = threads_per_socket

    @property
    def is_hyper_threading_enabled(self):
        """
        **[Required]** Gets the is_hyper_threading_enabled of this HostConfigurationSummary.
        Indicates if hyper-threading is enabled or not


        :return: The is_hyper_threading_enabled of this HostConfigurationSummary.
        :rtype: bool
        """
        return self._is_hyper_threading_enabled

    @is_hyper_threading_enabled.setter
    def is_hyper_threading_enabled(self, is_hyper_threading_enabled):
        """
        Sets the is_hyper_threading_enabled of this HostConfigurationSummary.
        Indicates if hyper-threading is enabled or not


        :param is_hyper_threading_enabled: The is_hyper_threading_enabled of this HostConfigurationSummary.
        :type: bool
        """
        self._is_hyper_threading_enabled = is_hyper_threading_enabled

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this HostConfigurationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this HostConfigurationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this HostConfigurationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this HostConfigurationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this HostConfigurationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this HostConfigurationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this HostConfigurationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this HostConfigurationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
