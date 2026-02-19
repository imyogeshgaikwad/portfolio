from django.core.management.base import BaseCommand
from portfolio.models import PortfolioItem


class Command(BaseCommand):
    help = 'Seed the database with Yogesh Gaikwad portfolio data'

    def handle(self, *args, **options):
        # Clear existing data
        PortfolioItem.objects.all().delete()
        self.stdout.write('Cleared existing portfolio items...')

        items = [
            # Profile
            {
                'category': 'profile',
                'title': 'Yogesh Gaikwad',
                'subtitle': 'Full-Stack Engineer',
                'description': '''
                    <p class="mb-2">📍 Dublin, Ireland</p>
                    <p class="mb-2">📧 imyogeshgaikwad@gmail.com</p>
                    <p class="mb-2">📱 +353 87 492 5777</p>
                    <p class="mb-2">🛂 Stamp 1G — Available Immediately</p>

                    <p class="mt-4 leading-relaxed">
                        Full-Stack Engineer with 3 years of commercial experience in TypeScript, Node.js, and React.
                        Built and shipped backend systems and APIs that cut operational effort by 60% and improved
                        system reliability by 41%. Comfortable working in Agile teams, shipping features end-to-end,
                        and picking up new tech fast.
                    </p>
                ''',
                'order': 1,
            },

            # Education
            {
                'category': 'education',
                'title': 'MSc in Information Systems with Computing',
                'subtitle': 'Dublin Business School (DBS), Ireland',
                'description': '''
                    <p class="mb-2">Graduating February 2026.</p>
                ''',
                'date_start': 'Apr 2024',
                'date_end': 'Feb 2026',
                'order': 1,
            },
            {
                'category': 'education',
                'title': 'Bachelor of Technology in Information Technology',
                'subtitle': 'SVKM Institute of Technology, India',
                'description': '''
                    <p class="mb-2"><strong>Focus Areas:</strong></p>
                    <ul class="list-disc list-inside space-y-1">
                        <li>Data Structures</li>
                        <li>Object-Oriented Programming (Java/Python)</li>
                        <li>Software Engineering</li>
                    </ul>
                ''',
                'date_start': 'Aug 2019',
                'date_end': 'Feb 2023',
                'order': 2,
            },

            # Experience
            {
                'category': 'experience',
                'title': 'Full-Stack Software Engineer',
                'subtitle': 'Tata Communications',
                'description': '''
                    <ul class="list-disc list-inside space-y-2">
                        <li>Built TypeScript + Node.js backend with custom Dialogflow chatbot modules, improving chatbot response efficiency by <span class="text-green-400 font-bold">50%</span>.</li>
                        <li>Automated Google Sheets → Firebase data pipelines using Cloud Functions, eliminating <span class="text-green-400 font-bold">60%</span> of manual data entry effort.</li>
                        <li>Developed cloud-based APIs delivering rich responses in Google Chat, increasing user engagement by <span class="text-blue-400 font-bold">30%</span>.</li>
                        <li>Integrated Agent Assist for voice virtual agents, cutting customer response times by <span class="text-green-400 font-bold">15%</span>.</li>
                        <li>Delivered features across Agile Scrum sprints, managing tasks in Jira with consistent on-time delivery.</li>
                    </ul>
                ''',
                'date_start': 'Oct 2022',
                'date_end': 'Sep 2025',
                'technologies': 'TypeScript, Node.js, Dialogflow, Firebase, Cloud Functions, Google Chat API, Jira, Scrum',
                'order': 1,
            },
            {
                'category': 'experience',
                'title': 'Software Engineer (Intern)',
                'subtitle': 'Tata Elxsi',
                'description': '''
                    <ul class="list-disc list-inside space-y-2">
                        <li>Designed and implemented RESTful APIs for authentication, feedback, and issue reporting, achieving <span class="text-green-400 font-bold">99% uptime</span>.</li>
                        <li>Optimised middleware layer, reducing API response times by <span class="text-green-400 font-bold">35%</span> under high-traffic conditions.</li>
                        <li>Implemented Role-Based Access Control (RBAC), strengthening security and access compliance.</li>
                        <li>Built a React.js IoT dashboard for Tata Motors, reducing mean time to resolve production issues by <span class="text-blue-400 font-bold">41%</span>.</li>
                    </ul>
                ''',
                'date_start': 'Dec 2021',
                'date_end': 'Sep 2022',
                'technologies': 'REST APIs, Node.js, RBAC, Middleware, React.js, IoT',
                'order': 2,
            },

            # Projects
            {
                'category': 'project',
                'title': 'CAReader-AI',
                'subtitle': 'Full-Stack AI Web Application',
                'description': '''
                    <p class="mb-3">Full-stack web app with a <strong>TypeScript + Node.js</strong> backend,
                    AI-powered chatbot, REST APIs, JWT authentication, and a React/Next.js frontend.</p>
                    <p class="text-gray-400 text-sm">Reduced user search time by
                    <span class="text-green-400 font-bold">50%</span>.</p>
                    <p class="mt-3">
                        <a href="https://github.com/imyogeshgaikwad" target="_blank"
                           class="text-blue-400 hover:underline text-sm">🔗 View on GitHub →</a>
                    </p>
                ''',
                'technologies': 'TypeScript, Node.js, React.js, Next.js, REST APIs, JWT, AI Chatbot',
                'order': 1,
            },
            {
                'category': 'project',
                'title': 'Detecting-Humans-in-Fire',
                'subtitle': 'Python AI Safety System',
                'description': '''
                    <p class="mb-3">Python-based <strong>image recognition system</strong> for fire emergency
                    detection using FastAPI and TensorFlow, delivering real-time predictions via a REST API.</p>
                    <p class="mt-3">
                        <a href="https://github.com/imyogeshgaikwad" target="_blank"
                           class="text-blue-400 hover:underline text-sm">🔗 View on GitHub →</a>
                    </p>
                ''',
                'technologies': 'Python, FastAPI, TensorFlow, REST API, Image Recognition',
                'order': 2,
            },

            # Skills
            {
                'category': 'skill',
                'title': 'Backend & APIs',
                'subtitle': 'Core Server-Side Stack',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">TypeScript</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Node.js</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Express.js</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">REST APIs</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">JWT</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">RBAC</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Middleware</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">MVC</span>
                    </div>
                ''',
                'technologies': 'TypeScript, Node.js, Express.js, REST APIs, JWT, RBAC, Middleware, MVC',
                'order': 1,
            },
            {
                'category': 'skill',
                'title': 'Frontend',
                'subtitle': 'UI & Web Technologies',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">React.js</span>
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">Next.js</span>
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">HTML5</span>
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">CSS3</span>
                    </div>
                ''',
                'technologies': 'React.js, Next.js, HTML5, CSS3',
                'order': 2,
            },
            {
                'category': 'skill',
                'title': 'AI & Automation',
                'subtitle': 'Machine Learning & Bots',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Python</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">FastAPI</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">TensorFlow</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Dialogflow</span>
                    </div>
                ''',
                'technologies': 'Python, FastAPI, TensorFlow, Dialogflow',
                'order': 3,
            },
            {
                'category': 'skill',
                'title': 'Databases',
                'subtitle': 'Data Storage',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">PostgreSQL</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">MySQL</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">MongoDB</span>
                    </div>
                ''',
                'technologies': 'PostgreSQL, MySQL, MongoDB',
                'order': 4,
            },
            {
                'category': 'skill',
                'title': 'Cloud & DevOps',
                'subtitle': 'Infrastructure & Tooling',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">AWS (EC2, S3)</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Docker</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">CI/CD</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Git/GitHub</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Jira</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Scrum/Kanban</span>
                    </div>
                ''',
                'technologies': 'AWS, Docker, CI/CD, Git/GitHub, Jira, Scrum, Kanban',
                'order': 5,
            },
        ]

        for item_data in items:
            PortfolioItem.objects.create(**item_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(items)} portfolio items!'))