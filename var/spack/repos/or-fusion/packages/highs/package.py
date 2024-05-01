# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Highs(CMakePackage):
    """Highs optimization solver.
    """

    homepage = "https://github.com/ERGO-Code/HiGHS"
    url = "https://github.com/ERGO-Code/HiGHS/archive/refs/tags/v1.7.0.tar.gz"
    git = "https://github.com/ERGO-Code/HiGHS.git"
    maintainers("whart222")

    license("MIT")

    version("1.7.0", sha256="d10175ad66e7f113ac5dc00c9d6650a620663a6884fbf2942d6eb7a3d854604f")

    #variant("debug", default=False, description="Enable debugging")
    #variant("verbose", default=False, description="Enable verbose build")
    #variant("threads", default=True, description="Build with threads enabled")
    #variant("shared", default=True, description="Build shared library")

    #variant("tests", default=False, description="Build coek test executables")
    #variant("python", default=False, description="Build pycoek and install coek python libraries")
    #variant("compact", default=False, description="Build compact expressions in coek")

    #variant("openmp", default=True, description="Build with openmp")
    #variant("gurobi", default=False, description="Build with Gurobi optimization library")
    #variant("cppad", default=False, description="Build with the CppAD library")
    #variant("asl", default=False, description="Build with the ASL library")

    def cmake_args(self):
        spec = self.spec
        args = []

        args.append("-DFAST_BUILD=ON")

        return args
