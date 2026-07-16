import os
import json
import random
import subprocess
import time
from datetime import datetime
from openai import OpenAI

# Initialize API Client (Uses Environment Variable NVIDIA_API_KEY)
api_key = os.environ.get("NVIDIA_API_KEY")  # Default to provided key for local testing

client = OpenAI(
  base_url="https://integrate.api.nvidia.com/v1",
  api_key=api_key
)

# Style variations to ensure unique solutions each cycle
STYLE_VARIATIONS = [
    "Provide a clean, well-commented Python solution",
    "Provide an efficient Python solution with detailed inline comments explaining each step",
    "Provide a Python solution using a different approach than typical solutions, with clear comments",
    "Provide a concise and optimized Python solution with comments on time and space complexity",
    "Provide a readable Python solution with docstrings and type hints",
    "Provide a Python solution that prioritizes clarity and includes step-by-step comments",
    "Provide a Pythonic solution using built-in functions where possible, with comments",
    "Provide a well-structured Python solution with helper functions and comments",
]

def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return []

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def load_cycle_info(filepath='cycle_info.json'):
    """Load the current cycle number and metadata."""
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {"cycle": 1, "started_at": datetime.now().isoformat(), "total_solved": 0}

def save_cycle_info(info, filepath='cycle_info.json'):
    with open(filepath, 'w') as f:
        json.dump(info, f, indent=4)

def generate_solution(problem_title, cycle=1):
    """Generate a solution with style variation based on cycle number."""
    style = STYLE_VARIATIONS[(cycle - 1) % len(STYLE_VARIATIONS)]
    
    # Vary temperature slightly each cycle for different outputs
    temp = 0.2 + ((cycle - 1) % 5) * 0.1  # Cycles through 0.2, 0.3, 0.4, 0.5, 0.6
    
    prompt = f"{style} for the standard Data Structures and Algorithms problem: '{problem_title}'. Output ONLY the Python code without any markdown formatting, backticks, or explanations. Include comments in the code explaining the logic."
    
    # Add a cycle-specific comment request to ensure uniqueness
    if cycle > 1:
        prompt += f" Add a comment at the top: '# Solution approach {cycle} - {style.split(',')[0].lower()}'"
    
    completion = client.chat.completions.create(
      model="meta/llama-3.1-70b-instruct",
      messages=[{"content": prompt, "role": "user"}],
      temperature=temp,
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
        return True
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        print(e.stderr.decode('utf-8'))
        return False

def main():
    problems_file = 'problems.json'
    solved_file = 'solved.json'
    
    problems = load_json(problems_file)
    solved = load_json(solved_file)
    cycle_info = load_cycle_info()
    
    # Check for unsolved problems
    unsolved = [p for p in problems if p['slug'] not in solved]
    
    # If all problems are solved, reset and start a new cycle
    if not unsolved:
        cycle_info['cycle'] += 1
        cycle_info['started_at'] = datetime.now().isoformat()
        print(f"🔄 All problems solved! Starting cycle {cycle_info['cycle']}...")
        
        # Clear the solved list to start fresh
        solved = []
        save_json(solved_file, solved)
        unsolved = list(problems)  # All problems are now unsolved again
    
    current_cycle = cycle_info['cycle']
    print(f"📚 Cycle {current_cycle} | Unsolved: {len(unsolved)} | Total solved across all cycles: {cycle_info['total_solved']}")

    max_to_solve = min(15, len(unsolved))
    min_to_solve = min(8, max_to_solve)
    num_to_solve = random.randint(min_to_solve, max_to_solve)
    print(f"Planning to solve {num_to_solve} problems today.")
    
    selected_problems = random.sample(unsolved, num_to_solve)
    solved_today = 0
    
    for problem in selected_problems:
        title = problem['title']
        slug = problem['slug']
        print(f"Solving: {title}...")
        
        # Retry logic for API failures
        max_retries = 3
        for attempt in range(max_retries):
            try:
                solution_code = generate_solution(title, cycle=current_cycle)
                
                # Validate solution is not empty
                if not solution_code or len(solution_code) < 20:
                    print(f"  ⚠️ Generated solution too short, retrying... (attempt {attempt + 1})")
                    continue
                
                # Create a safe filename
                filename = f"{slug}.py"
                with open(filename, 'w') as f:
                    f.write(solution_code)
                
                print(f"  ✅ Saved {filename}")
                
                # Git commit with cycle info for unique commit messages
                commit_msg = f"Solved {title}"
                if current_cycle > 1:
                    commit_msg = f"Solved {title} (approach {current_cycle})"
                
                run_git_command(f'git add {filename} {solved_file}')
                run_git_command(f'git commit -m "{commit_msg}"')
                
                solved.append(slug)
                save_json(solved_file, solved)
                
                solved_today += 1
                cycle_info['total_solved'] += 1
                
                print(f"  📝 Committed: {title}")
                break  # Success, move to next problem
                
            except Exception as e:
                print(f"  ❌ Attempt {attempt + 1} failed for {title}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2)  # Brief pause before retry
                else:
                    print(f"  ⛔ Skipping {title} after {max_retries} failed attempts")
    
    # Save cycle info
    save_cycle_info(cycle_info)
    
    # Commit cycle info
    run_git_command('git add cycle_info.json')
    run_git_command('git diff --cached --quiet || git commit -m "Update cycle info"')
    
    print(f"\n🎯 Solved {solved_today} problems today (Cycle {current_cycle})")
    print("Pushing to GitHub...")
    run_git_command('git push')

if __name__ == "__main__":
    main()
