format_exclude := "''.*'' just.d"

# Formats the markdown files.
format:
	fd -e md --hidden `for item in {{format_exclude}}; do printf -- "--exclude %s " "$item"; done` --exec just _format

[private]
_format MD:
	mkdir -p .tmp/`dirname "{{MD}}"`
	cat {{MD}} | par -w 80 -j "-P=[-=>" > .tmp/{{MD}}.par && sleep 0.1 && mv .tmp/{{MD}}.par {{MD}}
	rm -rf .tmp
