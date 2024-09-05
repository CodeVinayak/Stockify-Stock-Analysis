const express = require('express');
const multer = require('multer');
const fs = require('fs');
const axios = require('axios');
const path = require('path');

const app = express();

// Multer configuration
const upload = multer({ dest: 'uploads/' });

// GitHub configuration
const GITHUB_TOKEN = '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';  // Replace with your GitHub token
const GITHUB_REPO = 'CodeVinayak/Stockify-Stock-Analysis';     // Replace with your repo (e.g., 'user/repo')
const GITHUB_PATH = 'path/to/data.csv';            // Path within the repo (e.g., 'data.csv')
const GITHUB_BRANCH = 'main';                      // Branch to commit to

// Endpoint to upload the CSV file
app.post('/upload', upload.single('file'), async (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }

    try {
        const filePath = path.join(__dirname, req.file.path);
        const content = fs.readFileSync(filePath, 'utf-8');
        const encodedContent = Buffer.from(content).toString('base64');

        // Get the SHA of the existing file (if it exists)
        const response = await axios.get(`https://api.github.com/repos/${GITHUB_REPO}/contents/${GITHUB_PATH}`, {
            headers: {
                'Authorization': `token ${GITHUB_TOKEN}`,
                'Accept': 'application/vnd.github.v3+json'
            }
        }).catch(() => null);  // Ignore errors (e.g., if file does not exist)

        const sha = response?.data?.sha;

        // Create or update the file in the repo
        await axios.put(`https://api.github.com/repos/${GITHUB_REPO}/contents/${GITHUB_PATH}`, {
            message: 'Upload CSV file',
            content: encodedContent,
            branch: GITHUB_BRANCH,
            sha: sha  // Include SHA only if the file already exists
        }, {
            headers: {
                'Authorization': `token ${GITHUB_TOKEN}`,
                'Accept': 'application/vnd.github.v3+json'
            }
        });

        res.send('File uploaded to GitHub successfully.');
    } catch (error) {
        console.error('Error uploading file to GitHub:', error);
        res.status(500).send('Failed to upload file to GitHub.');
    } finally {
        // Clean up the temporary file
        fs.unlinkSync(req.file.path);
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
