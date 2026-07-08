import os
import json
import random
import subprocess
from openai import OpenAI

# Initialize API Client (Uses Environment Variable NVIDIA_API_KEY)
api_key = os.environ.get("NVIDIA_API_KEY") # Default to provided key for local testing

client = OpenAI(
  base_url="https://integrate.api.nvidia.com/v1",
  api_key=api_key
)

def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return []

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def generate_solution(problem_title):
    prompt = f"Provide a Python solution for the standard Data Structures and Algorithms problem: '{problem_title}'. Output ONLY the Python code without any markdown formatting, backticks, or explanations. Include comments in the code explaining the logic."
    
    completion = client.chat.completions.create(
      model="meta/llama-3.1-70b-instruct",
      messages=[{"content": prompt, "role": "user"}],
      temperature=0.2,
      top_p=0.7,
      max_tokens=4096,
      stream=True
    )
    
    code = ""
    for chunk in completion:
        if chunk.choices and chunk.choices[0].delta.content is not None:
            code += chunk.choices[0].delta.content
            
    # Clean up any potential markdown backticks that the model might still add despite instructions
    code = code.strip()
    if code.startswith("```python"):
        code = code[9:]
    elif code.startswith("```"):
        code = code[3:]
    if code.endswith("```"):
        code = code[:-3]
        
    return code.strip()

def run_git_command(command):
    try:
        subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        print(e.stderr.decode('utf-8'))

def main():
    problems_file = 'problems.json'
    solved_file = 'solved.json'
    
    problems = load_json(problems_file)
    solved = load_json(solved_file)
    
    unsolved = [p for p in problems if p['slug'] not in solved]
    
    if not unsolved:
        print("All problems solved!")
        return



    max_to_solve = min(15, len(unsolved))
    min_to_solve = min(8, max_to_solve)
    num_to_solve = random.randint(min_to_solve, max_to_solve)
    print(f"Planning to solve {num_to_solve} problems today.")
    
    selected_problems = random.sample(unsolved, num_to_solve)
    
    for problem in selected_problems:
        title = problem['title']
        slug = problem['slug']
        print(f"Solving: {title}...")
        
        try:
            solution_code = generate_solution(title)
            
            # Create a safe filename
            filename = f"{slug}.py"
            with open(filename, 'w') as f:
                f.write(solution_code)
            
            print(f"Saved {filename}")
            
            # Git commit
            run_git_command(f'git add {filename} {solved_file}')
            run_git_command(f'git commit -m "Solved {title}"')
            
            solved.append(slug)
            save_json(solved_file, solved)
            
            print(f"Committed {title}")
            
        except Exception as e:
            print(f"Failed to solve {title}: {e}")

    print("Pushing to GitHub...")
    # git push - uncomment or let github actions handle it
    run_git_command('git push')

if __name__ == "__main__":
    main()
