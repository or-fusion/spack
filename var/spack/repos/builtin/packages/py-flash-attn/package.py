# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlashAttn(PythonPackage):
    """
    This package provides the official implementation of FlashAttention.
    """

    pypi = "flash-attn/flash_attn-2.5.4.tar.gz"

    maintainers("aurianer")

    license("BSD")

    version("2.5.5", sha256="751cee17711d006fe7341cdd78584af86a6239afcfe43b9ed11c84db93126267")
    version("2.5.4", sha256="d83bb427b517b07e9db655f6e5166eb2607dccf4d6ca3229e3a3528c206b0175")
    version("2.4.2", sha256="eb822a8c4219b610e9d734cbc8cd9ee4547f27433815a2b90dc1462766feefc1")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-torch+cuda")
        depends_on("ninja")
        depends_on("py-einops")
        depends_on("py-packaging")

    with default_args(type=("build", "link", "run")):
        depends_on("py-pybind11")

    depends_on("py-psutil", type="build")

    depends_on("python@3.7:", type=("build", "run"))
