# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LinkML schema project for common value sets. It consists primarily of LinkML enum (static and dynamic) definitions,
organized by domain


## Project Structure

### Schema Files

- Main schema: `src/valuesets/schema/valuesets.yaml` -- this just imports
- Schema modules in: `src/valuesets/schema/`
  - `core.yaml` - Core definitions
  - bio/
      - MORE TO COME
  - `healthcare.yaml` - Healthcare-related value sets
  - `investigation.yaml` - Investigation-related value sets
  - `statistics.yaml` - Statistics-related value sets
  - `types.yaml` - Type definitions

Note:  we will probably start nesting some of these more

## Editing

After every edit, always check you didn't make a mistake by running `just site`

Additionally, validate your schema changes with `just validate` to ensure they conform to LinkML specifications.

DO NOT edit generated artefacts

## Guidelines

- Enums should be organized by domain
- Using CamelCase for all enum names
- PERMISSIBLE_VALUES in upper case by default, except when existing standard exists

## Linking to ontology terms

- use `meaning:` to map to an ontology term
- use OBO preferantially
- use CURIEs, with prefixes declared in header.

ALWAYS check IDs, NEVER guess them. Use OLS to check.

## Development Commands

All commands are managed through the `just` command runner:

- **Run tests**: `just test`
- **Run linting**: `just lint`
- **Validate schema**: `just validate` - Validates LinkML schema definitions


### Generated Code
- Python datamodel: `src/valuesets/datamodel/`
  - Auto-generated from schema - do not edit directly
- Project artifacts: `project/` directory (git-ignored by default)

