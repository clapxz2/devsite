@echo off
echo 🚀 Starting deployment process...
echo ================================================

REM Add all files
echo 🔄 Adding files to git...
git add .
if %errorlevel% neq 0 (
    echo ❌ Failed to add files
    pause
    exit /b 1
)

REM Check if there are changes
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo ℹ️  No changes to commit
    pause
    exit /b 0
)

REM Commit changes
echo 🔄 Committing changes...
if "%1"=="" (
    git commit -m "Update dev showcase - %date% %time%"
) else (
    git commit -m "%*"
)
if %errorlevel% neq 0 (
    echo ❌ Failed to commit
    pause
    exit /b 1
)

REM Push to GitHub
echo 🔄 Pushing to GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo ❌ Failed to push
    pause
    exit /b 1
)

echo.
echo 🎉 Deployment completed successfully!
echo 🌐 Your changes are now live on GitHub
echo 📱 Check your Render deployment status
pause
