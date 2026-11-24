#version 330 compatibility

uniform sampler2D gtexture;
uniform sampler2D lightmap;
uniform sampler2D depthtex0;

uniform float viewHeight;
uniform float viewWidth;

in vec2 texcoord;
in vec2 lmcoord;
in vec4 glcolor;

/* RENDERTARGETS: 0 */
layout(location = 0) out vec4 color;

void main() {
	vec2 depthcoord = gl_FragCoord.xy / vec2(viewWidth, viewHeight);
    if (texture(depthtex0, depthcoord).r != 1.0) {
        discard;
    }

	color = texture(gtexture, texcoord) * glcolor;
	color *= texture(lightmap, lmcoord);
	if (color.a < 0.1) {
		discard;
	}
}
