#!/bin/bash
set -euo pipefail

REPO_DIR="/home/tharuneswar/DSA_Practice"
STREAK_LOG="$REPO_DIR/streak_log.txt"
TODAY=$(date -u +"%Y-%m-%d")

cd "$REPO_DIR" || { echo "ERROR: Cannot cd to $REPO_DIR"; exit 1; }

# Configure git if not set
git config user.name "Tharuneswar" 2>/dev/null || true
git config user.email "dtharuneswar@aditya.ac.in" 2>/dev/null || true

# Pull latest with retry
for i in 1 2 3; do
    git pull --rebase origin master 2>/dev/null && break || sleep 3
done

# Count commits today
TODAY_COUNT=$(git log --since="midnight UTC" --oneline 2>/dev/null | wc -l)
echo "Today's commits: $TODAY_COUNT"

# Skip if already at or above 20
if [ "$TODAY_COUNT" -ge 20 ]; then
    echo "Already have $TODAY_COUNT commits today. Skipping."
    exit 0
fi

# Calculate how many more we need
TARGET=15
NEEDED=$((TARGET - TODAY_COUNT))
if [ "$NEEDED" -le 0 ]; then
    echo "Already met target. Skipping."
    exit 0
fi

# Make 5-8 commits per run
MIN_COMMITS=5
MAX_COMMITS=8
NUM_COMMITS=$((RANDOM % (MAX_COMMITS - MIN_COMMITS + 1) + MIN_COMMITS))
if [ "$NUM_COMMITS" -gt "$NEEDED" ]; then
    NUM_COMMITS=$NEEDED
fi

echo "Making $NUM_COMMITS commits..."

COMMITTED=0
for i in $(seq 1 "$NUM_COMMITS"); do
    TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    echo "$TIMESTAMP - Daily streak maintained" >> "$STREAK_LOG"

    if git add streak_log.txt && git commit -m "Daily streak check - $TODAY" --quiet 2>/dev/null; then
        COMMITTED=$((COMMITTED + 1))
        echo "  Commit $COMMITTED/$NUM_COMMITS done"
    else
        echo "  Commit $i failed, retrying..."
        sleep 2
        git add streak_log.txt && git commit -m "Daily streak check - $TODAY" --quiet 2>/dev/null && COMMITTED=$((COMMITTED + 1)) || echo "  Skipped (no changes)"
    fi

    # Random sleep 2-8 seconds
    sleep $((RANDOM % 7 + 2))
done

echo "Made $COMMITTED commits."

# Push with retry
echo "Pushing to GitHub..."
for i in 1 2 3 4 5; do
    git pull --rebase origin master 2>/dev/null || true
    if git push origin master 2>/dev/null; then
        echo "Push succeeded."
        exit 0
    fi
    echo "Push attempt $i failed, retrying in $((i * 10))s..."
    sleep $((i * 10))
done

echo "ERROR: Push failed after 5 attempts"
exit 1
