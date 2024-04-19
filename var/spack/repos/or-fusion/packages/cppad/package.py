# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cppad(CMakePackage):
    """A Package for Differentiation of C++ Algorithms."""

    homepage = "https://www.coin-or.org/CppAD/"
    url = "https://github.com/coin-or/CppAD/archive/refs/tags/20240000.4.tar.gz"
    git = "https://github.com/coin-or/CppAD.git"

    version("20240000.4", sha256="0dfc1e30b32d5dd3086ee3adb6d2746a019e9d670b644c4d5ec1df3c35dd1fe5")
    version("20220000.5", sha256="9fb4562f6169855eadcd86ac4671593d1c0edf97bb6ce7cbb28e19af2bfc165e")

    def cmake_args(self):
        args = []

        args.append("-DCMAKE_ISNTALL_PREFIX=%s" % self.prefix)
        # This package does not obey CMAKE_INSTALL_PREFIX
        args.append("-Dcppad_prefix=%s" % self.prefix)

        args.append("-DCMAKE_BUILD_TYPE=Release")

        return args
