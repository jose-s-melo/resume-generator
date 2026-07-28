from generator import generator, parser, renderer

def main():
    data = parser.load_data("data/resume-example.yml")
    html = renderer.render_template(data)
    generator.generate(html)
    print("Success.")
    
if __name__ == "__main__":
    main()