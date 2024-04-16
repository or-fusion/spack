from spack.package import *


class Coek(CMakePackage, PythonExtension):
    """coek optimization monorepo, which installs libcoek, pycoek, and various
    python packages (especially poek).
    """

    homepage = "https://github.com/sandialabs/coek"
    url = "https://github.com/sandialabs/coek/archive/refs/tags/1.4.0.tar.gz"
    git = "git@github.com:sandialabs/coek.git"
    maintainers("whart222")

    license("BSD")

    version("1.4.0", sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    version("main", branch="main")
    version("dev", branch="dev")
    version("dev-weh", branch="dev-weh")

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20", conditional("23", when="^cmake@3.20.3:")),
        multi=False,
        description="Use the specified C++ standard when building",
    )
    variant("debug", default=False, description="Enable debugging")
    variant("verbose", default=False, description="Enable verbose build")
    variant("threads", default=True, description="Build with threads enabled")
    variant("shared", default=True, description="Build shared library")
    variant("pic", default=True, description="Build position-independent code")

    variant("tests", default=False, description="Build coek test executables")
    variant("python", default=False, description="Build pycoek and install coek python libraries")
    variant("compact", default=False, description="Build compact expressions in coek")

    variant("tpls", default=True, description="Build with all dependencies")
    variant("openmp", default=True, description="Build with openmp")
    variant("gurobi", default=False, description="Build with Gurobi optimization library")
    variant("cppad", default=False, description="Build with the CppAD library")
    variant("asl", default=False, description="Build with the ASL library")

    #gcov
    #gprof
    #caliper
    depends_on("cmake@3.13.0:", type="build")
    depends_on("catch2@2.13.6", when="+tests")
    with when("+python"):
        depends_on("py-pip", type="build")
        depends_on("py-pybind11@2.10.4")
        extends("python")
    depends_on("fmt@8.0.1")
    depends_on("rapidjson@1.1.0")
    #with when("+tpls"):
    #    depends_on("cppad")
    #    depends_on("asl")
    #with when("+cppad"):
    #    depends_on("cppad")
    #with when("+asl"):
    #    depends_on("asl")

    def setup_run_environment(self, env):
        if '+python' in self.spec:
            env.append_path('PYTHONPATH', self.spec.prefix.python)

    def cmake_args(self):
        spec = self.spec
        args = []

        args.append("-Dwith_spack=ON")

        args.append("-Dwith_fmtlib=ON")
        args.append("-Dwith_rapidjson=ON")

        if self.spec.satisfies("+shared"):
            args.append("-DBUILD_SHARED_LIBS=ON")
        elif self.spec.satisfies("-shared"):
            args.append("-DBUILD_SHARED_LIBS=OFF")
        if self.spec.satisfies("+debug"):
            args.append("-Dwith_debug=ON")
        if self.spec.satisfies("+verbose"):
            args.append("-Dwith_verbose=ON")
        if self.spec.satisfies("+threads"):
            args.append("-Dwith_threads=ON")
        if self.spec.satisfies("+openmp"):
            args.append("-Dwith_openmp=ON")
        if self.spec.satisfies("+tests"):
            args.append("-Dwith_tests=ON")
            args.append("-Dwith_catch2=ON")
        if self.spec.satisfies("+python"):
            args.append("-Dwith_python=ON")
            args.append("-Dwith_pybind11=ON")
        if self.spec.satisfies("+compact"):
            args.append("-Dwith_compact=ON")

        #
        # External gurobi dependency found by CMAKE, not spack
        #
        if self.spec.satisfies("+gurobi"):
            args.append("-Dwith_gurobi=ON")

        # Require standard at configure time to guarantee the
        # compiler supports the selected standard.
        args.append("-DCMAKE_CXX_STANDARD_REQUIRED=ON")
        args.append("-DCMAKE_CXX_STANDARD={0}".format(spec.variants["cxxstd"].value))

        ## Don't build tests
        #args.append(self.define("FMT_TEST", self.run_tests))

        return args
