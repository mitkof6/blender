# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

import re


_valid_before = "(?<=[\\s*'\"`])|(?<=[a-zA-Z][/-])|(?<=^)"
_valid_after = "(?=[\\s'\"`.!?,;:])|(?=[/-]\\s*[a-zA-Z])|(?=$)"
_valid_words = "(?:{})(?:(?:[A-Z]+[a-z]*)|[A-Z]*|[a-z]*)(?:{})".format(_valid_before, _valid_after)
_reg = re.compile(_valid_words)


def split_words(text):
    return [w for w in _reg.findall(text) if w]


# These must be all lower case for comparisons
dict_uimsgs = {
    # OK words
    "aren",  # aren't
    "betweens",  # yuck! in-betweens!
    "boolean", "booleans",
    "decrement",
    "doesn",  # doesn't
    "fader",
    "hoc",  # ad-hoc
    "indices",
    "iridas",
    "isn",  # isn't
    "iterable",
    "kyrgyz",
    "latin",
    "merchantability",
    "mplayer",
    "vertices",

    # Merged words
    "addon", "addons",
    "antialiasing",
    "arcsine", "arccosine", "arctangent",
    "autoclip",
    "autocomplete",
    "autoname",
    "autosave",
    "autoscale",
    "autosmooth",
    "autosplit",
    "backface", "backfacing",
    "backimage",
    "backscattered",
    "bandnoise",
    "bindcode",
    "bitrate",
    "blendin",
    "bonesize",
    "boundbox",
    "boxpack",
    "buffersize",
    "builtin", "builtins",
    "chunksize",
    "de",
    "defocus",
    "denoise",
    "despill", "despilling",
    "filebrowser",
    "filelist",
    "filename", "filenames",
    "filepath", "filepaths",
    "forcefield", "forcefields",
    "fulldome", "fulldomes",
    "fullscreen",
    "gridline",
    "hemi",
    "inscatter",
    "lightless",
    "lookup", "lookups",
    "mathutils",
    "midlevel",
    "midground",
    "mixdown",
    "multi",
    "multifractal",
    "multires", "multiresolution",
    "multisampling",
    "multitexture",
    "namespace",
    "keyconfig",
    "playhead",
    "polyline",
    "popup", "popups",
    "pre",
    "precalculate",
    "prefetch",
    "premultiply", "premultiplied",
    "prepass",
    "prepend",
    "preprocess", "preprocessing",
    "preseek",
    "readonly",
    "realtime",
    "rekey",
    "remesh",
    "reprojection",
    "resize",
    "restpose",
    "retarget", "retargets", "retargeting", "retargeted",
    "ringnoise",
    "rolloff",
    "screencast", "screenshot", "screenshots",
    "selfcollision",
    "singletexture",
    "startup",
    "stateful",
    "starfield",
    "subflare", "subflares",
    "subframe", "subframes",
    "subclass", "subclasses", "subclassing",
    "subdirectory", "subdirectories", "subdir", "subdirs",
    "submodule", "submodules",
    "subpath",
    "subsize",
    "substep", "substeps",
    "targetless",
    "textbox", "textboxes",
    "tilemode",
    "timestamp", "timestamps",
    "timestep", "timesteps",
    "un",
    "unbake",
    "uncomment",
    "undeformed",
    "undistort", "undistortion",
    "ungroup",
    "unhide",
    "unindent",
    "unkeyed",
    "unpremultiply",
    "unprojected",
    "unreacted",
    "unregister",
    "unselected",
    "unsubdivided",
    "unshadowed",
    "unspill",
    "unstitchable",
    "vectorscope",
    "worldspace",
    "workflow",

    # Neologisms, slangs
    "automagic", "automagically",
    "blobby",
    "blockiness", "blocky",
    "collider", "colliders",
    "deformer", "deformers",
    "determinator",
    "editability",
    "keyer",
    "lacunarity",
    "numerics",
    "occluder",
    "passepartout",
    "perspectively",
    "polygonization",
    "selectability",
    "slurph",
    "trackability",
    "transmissivity",
    "rasterized", "rasterization",
    "renderer", "renderable", "renderability",

    # Abbreviations
    "aero",
    "amb",
    "anim",
    "bool",
    "calc",
    "config", "configs",
    "const",
    "coord", "coords",
    "degr",
    "dof",
    "dupli", "duplis",
    "eg",
    "esc",
    "expr",
    "fac",
    "fra",
    "frs",
    "grless",
    "http",
    "init",
    "kbit",
    "lensdist",
    "loc", "rot", "pos",
    "lorem",
    "luma",
    "multicam",
    "num",
    "ok",
    "orco",
    "ortho",
    "persp",
    "pref", "prefs",
    "prev",
    "param",
    "premul",
    "quad", "quads",
    "quat", "quats",
    "recalc", "recalcs",
    "refl",
    "spec",
    "struct", "structs",
    "tex",
    "tri", "tris",
    "uv", "uvs", "uvw", "uw", "uvmap",
    "vec",
    "vert", "verts",
    "vis",
    "xyz", "xzy", "yxz", "yzx", "zxy", "zyx",
    "xy", "xz", "yx", "yz", "zx", "zy",

    # General computer/science terms
    "boid", "boids",
    "equisolid",
    "euler", "eulers",
    "hashable",
    "intrinsics",
    "isosurface",
    "jitter", "jittering", "jittered",
    "keymap", "keymaps",
    "lambertian",
    "laplacian",
    "metadata",
    "nand", "xnor",
    "normals",
    "numpad",
    "octree",
    "opengl",
    "pulldown", "pulldowns",
    "quantized",
    "samplerate",
    "scrollback",
    "scrollbar",
    "scroller",
    "searchable",
    "spacebar",
    "tooltip", "tooltips",
    "trackpad",
    "unicode",
    "viewport", "viewports",
    "viscoelastic",
    "wildcard", "wildcards",

    # General computer graphics terms
    "anaglyph",
    "bezier", "beziers",
    "bicubic",
    "bilinear",
    "blackpoint", "whitepoint",
    "blinn",
    "bokeh",
    "catadioptric",
    "centroid",
    "chrominance",
    "codec", "codecs",
    "collada",
    "compositing",
    "crossfade",
    "deinterlace",
    "dropoff",
    "eigenvectors",
    "equirectangular",
    "fisheye",
    "framerate",
    "gimbal",
    "grayscale",
    "icosphere",
    "lightmap",
    "lossless", "lossy",
    "midtones",
    "mipmap", "mipmaps", "mip",
    "ngon", "ngons",
    "nurb", "nurbs",
    "perlin",
    "phong",
    "radiosity",
    "raytrace", "raytracing", "raytraced",
    "renderfarm",
    "shader", "shaders",
    "specular", "specularity",
    "spillmap",
    "sobel",
    "tonemap",
    "toon",
    "timecode",
    "voronoi",
    "voxel", "voxels",
    "wireframe",
    "zmask",
    "ztransp",

    # Blender terms
    "bbone",
    "breakdowner",
    "bspline",
    "bweight",
    "colorband",
    "datablock", "datablocks",
    "dopesheet",
    "dupliface", "duplifaces",
    "dupliframe", "dupliframes",
    "dupliobject", "dupliob",
    "dupligroup",
    "duplivert",
    "fcurve", "fcurves",
    "fluidsim",
    "frameserver",
    "enum",
    "keyframe", "keyframes", "keyframing", "keyframed",
    "metaball", "metaballs",
    "metaelement", "metaelements",
    "metastrip", "metastrips",
    "movieclip",
    "nabla",
    "navmesh",
    "outliner",
    "paintmap", "paintmaps",
    "polygroup", "polygroups",
    "poselib",
    "pushpull",
    "pyconstraint", "pyconstraints",
    "shapekey", "shapekeys",
    "shrinkfatten",
    "shrinkwrap",
    "softbody",
    "stucci",
    "sunsky",
    "subsurf",
    "texface",
    "timeline", "timelines",
    "tosphere",
    "vcol", "vcols",
    "vgroup", "vgroups",
    "vinterlace",
    "wetmap", "wetmaps",
    "wpaint",

    # Algorithm names
    "beckmann",
    "catmull",
    "catrom",
    "chebychev",
    "kutta",
    "lennard",
    "minkowsky",
    "minnaert",
    "musgrave",
    "nayar",
    "netravali",
    "oren",
    "prewitt",
    "runge",
    "verlet",
    "worley",

    # Acronyms
    "aa", "msaa",
    "api",
    "asc", "cdl",
    "ascii",
    "atrac",
    "bw",
    "ccd",
    "cmd",
    "cpus",
    "ctrl",
    "cw", "ccw",
    "dev",
    "djv",
    "dpi",
    "dvar",
    "dx",
    "fh",
    "fov",
    "fft",
    "gfx",
    "gl",
    "glsl",
    "gpl",
    "gpu", "gpus",
    "hc",
    "hdr",
    "hh", "mm", "ss", "ff", # hh:mm:ss:ff timecode
    "hsv", "hsva",
    "id",
    "itu",
    "lhs",
    "lmb", "mmb", "rmb",
    "mux",
    "ndof",
    "ppc",
    "px",
    "qmc",
    "rgb", "rgba",
    "rhs",
    "rv",
    "sdl",
    "sl",
    "smpte",
    "svn",
    "ui",
    "unix",
    "vbo", "vbos",
    "ycc", "ycca",
    "yuv", "yuva",

    # Blender acronyms
    "bge",
    "bli",
    "bvh",
    "dbvt",
    "dop",  # BLI K-Dop BVH
    "ik",
    "nla",
    "qbvh",
    "rna",
    "rvo",
    "simd",
    "sph",
    "svbvh",

    # CG acronyms
    "ao",
    "bsdf",
    "ior",
    "mocap",

    # Files types/formats
    "avi",
    "attrac",
    "autodesk",
    "bmp",
    "btx",
    "cineon",
    "dpx",
    "dxf",
    "eps",
    "exr",
    "fbx",
    "ffmpeg",
    "flac",
    "gzip",
    "ico",
    "jpg", "jpeg",
    "matroska",
    "mdd",
    "mkv",
    "mpeg", "mjpeg",
    "mtl",
    "ogg",
    "openjpeg",
    "piz",
    "png",
    "po",
    "quicktime",
    "rle",
    "sgi",
    "stl",
    "svg",
    "targa", "tga",
    "tiff",
    "theora",
    "vorbis",
    "wav",
    "xiph",
    "xml",
    "xna",
    "xvid",
}
